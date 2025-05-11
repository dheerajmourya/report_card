from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=50, unique=True)
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'yourapp_student'  # preserves the original table name if renaming

    def __str__(self):
        return f"{self.name} ({self.roll_number})"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class ReportCard(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='report_cards')
    total_marks = models.IntegerField()
    percentage = models.FloatField()
    overall_grade = models.CharField(max_length=5)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report Card - {self.student.name} ({self.percentage}%)"


class ReportCardSubject(models.Model):
    report_card = models.ForeignKey(ReportCard, on_delete=models.CASCADE, related_name='report_card_subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.subject.name} - {self.marks} Marks - Grade {self.grade}"
