📚 LMS – Learning Progress Tracking System

An industry-oriented Learning Management System (LMS) built with Django to track learner progress across structured courses and modules.
This project focuses on learning analytics, progress visualization, and admin-driven content management, similar to modern enterprise LMS platforms.

🚀 Project Overview

The LMS – Learning Tracker enables organizations, institutions, or training providers to:

Manage courses and modules

Track individual learner progress

Visualize completion percentages

Maintain structured learning paths

Monitor learning outcomes via an intuitive dashboard

This project is designed with real-world LMS architecture and is suitable for academic evaluation as well as portfolio demonstration.

🛠️ Tech Stack

Backend: Python, Django 6.0

Frontend: HTML5, CSS3, Bootstrap

Database: SQLite (development)

Authentication: Django Admin & Auth System

Version Control: Git & GitHub

✨ Key Features

🔐 Secure admin authentication

📘 Course management

📂 Module-wise learning structure

📊 Learning progress tracking

📈 Dynamic progress percentage calculation

🖥️ Clean and professional dashboard UI

⚙️ Scalable Django project structure

📂 Project Structure

lms/                          # Project root (pushed to GitHub)
│
├── lms/                      # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── lms_core/                 # Core LMS (Track Learning) app
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── dashboard.html   # Learning Progress Dashboard UI
│   ├── __init__.py
│   ├── admin.py             # Admin registrations
│   ├── apps.py              # App configuration
│   ├── models.py            # Course, Module, LearningProgress models
│   ├── views.py             # Dashboard logic
│   └── urls.py              # App routing
│
├── db.sqlite3                # Database (demo/testing)
├── manage.py                 # Django entry point
├── README.md                 # Project documentation
└── .gitignore                # Git ignored files



📊 Dashboard Preview

The dashboard displays:

Course name

Learner details

Completed modules

Visual progress bar

Completion percentage

(Inspired by professional LMS platforms used in industry training environments)

⚙️ Installation & Setup
# Clone the repository
git clone [https://github.com/<your-username>/lms-track-learning.git](https://github.com/Madhumitxx13/lms-track-learning/tree/main)

# Navigate to project
cd lms_project

# Create & activate virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver


Access:

Admin Panel: http://127.0.0.1:8000/admin/

Dashboard: http://127.0.0.1:8000/dashboard/

🎯 Use Cases

Corporate training platforms

Educational institutions

Skill-development programs

Employee onboarding & upskilling

Internship & certification tracking

🔮 Future Enhancements

Role-based access (Student / Trainer / Admin)

REST API integration

Course enrollment system

Graph-based analytics

Cloud database support

Responsive UI enhancements

👩‍💻 Author

Madhumitha S
Learning Management System – Industry Based Project
Built with a focus on scalability, clarity, and real-world LMS design

⭐ Acknowledgment

This project was developed as part of an industry-aligned LMS learning tracker, emphasizing practical implementation over basic CRUD systems.
