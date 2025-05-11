from django.contrib import admin
from .models import Students, Subject, ReportCard, ReportCardSubject


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'class_name', 'section')
    search_fields = ('name', 'roll_number')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_marks', 'percentage', 'overall_grade')
    search_fields = ('student__name', 'student__roll_number')


@admin.register(ReportCardSubject)
class ReportCardSubjectAdmin(admin.ModelAdmin):
    list_display = ('report_card', 'subject', 'marks', 'grade')
