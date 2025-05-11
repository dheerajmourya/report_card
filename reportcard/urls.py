from django.urls import path

from reportcard import views

urlpatterns = [


    path('students/', views.student_list, name='student_list'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('create/', views.create_report_card, name='create_report_card'),
    path('preview/<int:report_card_id>/', views.preview_report_card, name='preview_report_card'),
    path('download/<int:report_card_id>/', views.download_pdf, name='download_pdf'),
    path('edit/<int:report_card_id>/', views.edit_report_card, name='edit_report_card'),

 
]