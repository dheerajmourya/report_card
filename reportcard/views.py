from django.shortcuts import render, redirect, get_object_or_404
from .models import Students, Subject, ReportCard, ReportCardSubject
from .utils import calculate_grade
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages 

def student_list(request):
    students = Students.objects.all().order_by('-id')  
    return render(request, 'students_list.html', {'students': students})

def delete_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    student.delete()
    messages.success(request, f"Student '{student.name}' deleted successfully.")
    return redirect('student_list')

def create_report_card(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        class_name = request.POST['class']
        section = request.POST['section']
        comments = request.POST['comments']
        subjects = request.POST.getlist('subject[]')
        marks_list = request.POST.getlist('marks[]')

        #Check for duplicate roll number
        if Students.objects.filter(roll_number=roll).exists():
            messages.error(request, f'Roll number {roll} already exists. Please use a unique roll number.')
            return redirect('create_report_card')  # 🔁 Redirect so message hides after refresh

        # Create new student
        student = Students.objects.create(
            name=name,
            roll_number=roll,
            class_name=class_name,
            section=section
        )

        total = 0
        report_card = ReportCard.objects.create(
            student=student,
            total_marks=0,
            percentage=0,
            overall_grade='',
            comments=comments
        )

        for sub, mark in zip(subjects, marks_list):
            subject_obj, _ = Subject.objects.get_or_create(name=sub)
            mark = int(mark)
            grade = calculate_grade(mark)
            total += mark

            ReportCardSubject.objects.create(
                report_card=report_card,
                subject=subject_obj,
                marks=mark,
                grade=grade
            )

        percentage = total / len(subjects)
        final_grade = calculate_grade(percentage)

        report_card.total_marks = total
        report_card.percentage = percentage
        report_card.overall_grade = final_grade
        report_card.save()

        # messages.success(request, f'Report card for {name} created successfully!')
        return redirect('preview_report_card', report_card.id)

    return render(request, 'create_report_card.html')

def preview_report_card(request, report_card_id):
    report = get_object_or_404(ReportCard, id=report_card_id)
    return render(request, 'preview_report_card.html', {'report': report})

def download_pdf(request, report_card_id):
    report = get_object_or_404(ReportCard, id=report_card_id)
    template_path = 'report_card_pdf.html'
    context = {'report': report}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report_card.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa.CreatePDF(html, dest=response)
    return response



def edit_report_card(request, report_card_id):
    report = get_object_or_404(ReportCard, id=report_card_id)
    student = report.student
    subjects_data = report.report_card_subjects.all()

    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        class_name = request.POST['class']
        section = request.POST['section']
        comments = request.POST['comments']
        subjects = request.POST.getlist('subject[]')
        marks_list = request.POST.getlist('marks[]')

        # Check if another student has the same roll number
        if Students.objects.filter(roll_number=roll).exclude(id=student.id).exists():
            messages.error(request, f"Roll number {roll} already exists for another student.")
            return redirect('edit_report_card', report_card_id=report.id)

        # Update student info
        student.name = name
        student.roll_number = roll
        student.class_name = class_name
        student.section = section
        student.save()

        # Update report card
        report.comments = comments
        report.report_card_subjects.all().delete()

        total = 0
        for sub, mark in zip(subjects, marks_list):
            subject_obj, _ = Subject.objects.get_or_create(name=sub)
            mark = int(mark)
            grade = calculate_grade(mark)
            total += mark

            ReportCardSubject.objects.create(
                report_card=report,
                subject=subject_obj,
                marks=mark,
                grade=grade
            )

        percentage = total / len(subjects)
        final_grade = calculate_grade(percentage)

        report.total_marks = total
        report.percentage = percentage
        report.overall_grade = final_grade
        report.save()

        return redirect('preview_report_card', report.id)

    return render(request, 'edit_report_card.html', {
        'report': report,
        'student': student,
        'subjects': subjects_data
    })
