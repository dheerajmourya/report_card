# Report Card System

A student report card manager built with Django, supporting HTML form input and downloadable PDF generation for school use.

---

## Features

- Create student profiles with roll number, class, section
- Add subjects dynamically and enter marks
- Auto-grade calculation (A, B, C, etc.)
- View report card in browser
- Download report card as PDF
- Edit/Delete report cards
- List all students with report access
- Secure config using `.env`

---

## Technologies Used

- Django 4+
- SQLite (default)
- xhtml2pdf (for PDF generation)
- HTML/CSS 
- Python 3.11+

---


## Guiding Questions for Candidate --answers-

1. 🗄️ Database Schema
Q: What are the tables you’ll need? How will students and subjects relate?
Ans:
The following tables (models) are required: 
Students:-	Stores student info (name, roll number, class, section)
Subject:-	Stores subject names
ReportCard:-	Stores report info like total marks, percentage, grade
ReportCardSubject:-	Connects report card to subjects with marks and grades

Relationships:

A student can have multiple report cards
A report card is linked to multiple subjects via ReportCardSubject
ReportCardSubject contains marks + grade for each subject


Q: How will you determine the grade based on marks (e.g., A+, A, B, etc.)?

Ans:
We use a simple Python utility function to calculate grades based on marks:

def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'



3. PDF Generation
Q: How will you convert the report card to a downloadable PDF file?
Ans:
We use the xhtml2pdf library:
Render a Django template (report_card_pdf.html) with all student/report data
Pass the HTML to xhtml2pdf.pisa.CreatePDF() function
Return the PDF as a response to the user


from xhtml2pdf import pisa

def generate_pdf(request, report_card_id):
    template = get_template('report_card_pdf.html')
    html = template.render({'report_card': report})
    response = HttpResponse(content_type='application/pdf')
    pisa.CreatePDF(html, dest=response)
    return response


4. API Endpoints


Q: How will you structure the API responses, and what will the data look like?
A:
If extended to API (using Django REST Framework), these endpoints would be defined:


/api/students/	(GET)	 List all students
/api/report-card/create/	(POST)	Submit new report card
/api/report-card/<id>/	(GET)	 Get single report card details
/api/report-card/<id>/pdf/	 (GET)	Download report card as PDF



JSON Response:
{
  "student": {
    "name": "Rahul",
    "roll_number": "102",
    "class_name": "10",
    "section": "A"
  },
  "report_card": {
    "total_marks": 450,
    "percentage": 90,
    "overall_grade": "A+",
    "subjects": [
      {"name": "Math", "marks": 95, "grade": "A+"},
      {"name": "Science", "marks": 90, "grade": "A+"}
    ]
  }
}


## Final Deliverables (As Required in Task)

1.Database Schema: Define tables and relationships
We will use 4 core tables (models) to manage report card functionality:

Students:-	Stores student info: name, roll number, class, section
Subject:-	Stores subject names (e.g., Math, English)
ReportCard:-	Stores performance summary: total marks, percentage, grade
ReportCardSubject:-Connects ReportCard to Subject with marks & grade per subject


2. API Design: Define the API structure with response formats
( future-ready — based on Django REST Framework)

/api/students/	(GET)	 List all students
/api/report-card/create/	(POST)	Submit new report card
/api/report-card/<id>/	(GET)	 Get single report card details
/api/report-card/<id>/pdf/	 (GET)	Download report card as PDF


JSON Response:
{
  "student": {
    "name": "Aman",
    "roll_number": "105",
    "class_name": "9",
    "section": "B"
  },
  "report_card": {
    "total_marks": 420,
    "percentage": 84,
    "overall_grade": "A",
    "subjects": [
      { "name": "Math", "marks": 88, "grade": "A" },
      { "name": "Science", "marks": 90, "grade": "A+" }
    ]
  }
}


3. System Flow: From student data to report card generation
This explains how the system works step-by-step:

Step 1: User opens HTML form to enter student details and subject-wise marks

Step 2: On form submit:
    - Student entry is created (if roll number is unique)
    - A new ReportCard is generated for that student
    - For each subject:
        - Subject is created/reused
        - Marks are saved with grade into ReportCardSubject

Step 3: Total marks and percentage are calculated automatically
    - Grade is assigned based on percentage using logic

Step 4: ReportCard is saved and user is redirected to preview page

Step 5: From preview page, user can:
    - Edit report card
    - Download report card as a PDF using xhtml2pdf

Step 6: PDF is rendered using HTML + data and returned as downloadable file



## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/report-card-django.git
cd report-card-django




## Project Structure   


report_card_project/
├── manage.py
├── .env
├── requirements.txt
├── README.md
├── report_card_project/ # django project settings
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── reportcard/ # django app
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── utils.py
│ └── templates/
│ ├── create_report_card.html
│ ├── edit_report_card.html
│ ├── preview_report_card.html
│ ├── student_list.html
│ └── report_card_pdf.html