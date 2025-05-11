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