<div align="center">

# 📚 LMS Track Learning

### Django-Powered Learning Management System with Progress Analytics

[![Python](https://img.shields.io/badge/Python-68.6%25-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)
[![HTML5](https://img.shields.io/badge/HTML5-31.4%25-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-UI%20Framework-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)

**A production-grade Learning Management System that enables organizations to manage structured course content, track individual learner progress in real time, and visualize completion analytics through a clean, intuitive dashboard.**

[Overview](#overview) · [Features](#features) · [Architecture](#architecture) · [Data Models](#data-models) · [Quick Start](#quick-start) · [Dashboard](#dashboard) · [Roadmap](#roadmap)

</div>

---

## Overview

**LMS Track Learning** is an industry-oriented Learning Management System built with Django 6.0. It provides a complete workflow for course administration and learner progress tracking — from creating structured course content to monitoring module-level completion percentages across an organization.

The system is architected around three core entities: **Courses**, **Modules**, and **Learning Progress** — giving administrators fine-grained control over content structure while exposing clear, percentage-based progress metrics for every learner.

### Who It's For

| User | Role |
|---|---|
| **Administrators** | Create and manage courses, define module sequences, review learner data |
| **Organizations** | Monitor team-wide learning outcomes via the dashboard |
| **Institutions** | Track student progress across structured academic modules |
| **Training Providers** | Deliver and measure corporate upskilling programs |

---

## Features

### 🔐 Secure Authentication
Django's built-in authentication and admin system provides a secure, battle-tested login layer. Admin users manage all content and learner records through Django's native admin interface, with no additional configuration required.

### 📘 Course Management
Administrators can create courses with descriptive metadata, organize them into ordered modules, and publish them for learner enrollment — all through the Django admin panel.

### 📂 Module-Wise Learning Structure
Each course is broken into discrete modules, allowing granular tracking at the learning-unit level. Modules form an ordered sequence that defines the expected learning path for every enrolled learner.

### 📊 Progress Tracking Engine
The `LearningProgress` model records which modules each learner has completed, enabling the system to compute a dynamic **completion percentage** per learner per course. Progress is calculated as:

```
Completion % = (Completed Modules / Total Modules in Course) × 100
```

### 📈 Analytics Dashboard
A dedicated dashboard view (`/dashboard/`) aggregates and visualizes progress data, displaying for each enrolled learner:
- Course name
- Learner identity
- Number of modules completed vs. total
- Visual progress bar
- Percentage completion figure

### ⚙️ Scalable Django Architecture
The project follows Django's recommended app-based structure, separating project configuration (`lms/`) from application logic (`lms_core/`). This separation supports straightforward extension — adding new apps, REST APIs, or additional authentication layers without restructuring the core.

---

## Architecture

### Application Structure

```
lms-track-learning/
│
├── lms/                          # Django project configuration
│   ├── __init__.py
│   ├── asgi.py                   # ASGI entry point (async-ready)
│   ├── settings.py               # Project settings (DB, apps, middleware)
│   ├── urls.py                   # Root URL dispatcher
│   └── wsgi.py                   # WSGI entry point (production)
│
├── lms_core/                     # Core LMS application
│   ├── migrations/               # Database migration history
│   │   └── __init__.py
│   ├── templates/
│   │   └── dashboard.html        # Progress analytics dashboard UI
│   ├── __init__.py
│   ├── admin.py                  # Admin panel configuration for all models
│   ├── apps.py                   # App config (label: lms_core)
│   ├── models.py                 # Course, Module, LearningProgress models
│   ├── urls.py                   # App-level URL routing
│   └── views.py                  # Dashboard view logic & progress computation
│
├── db.sqlite3                    # SQLite database (development / demo)
├── manage.py                     # Django management entry point
├── README.md
└── .gitignore
```

### Request Flow

```
Browser Request
      │
      ▼
 urls.py (root)          ← lms/urls.py
      │
      ▼
 urls.py (app)           ← lms_core/urls.py
      │
      ▼
 views.py                ← Dashboard view queries LearningProgress
      │                     and annotates with completion %
      ▼
 models.py               ← ORM: Course → Module → LearningProgress
      │
      ▼
 db.sqlite3              ← SQLite persistence layer
      │
      ▼
 dashboard.html          ← Bootstrap-rendered progress table + bars
      │
      ▼
 Browser Response
```

---

## Data Models

The application is built on three primary Django models:

### `Course`
Represents a top-level learning program.

| Field | Type | Description |
|---|---|---|
| `title` | CharField | Course name |
| `description` | TextField | Course summary |
| `created_at` | DateTimeField | Auto-set creation timestamp |

### `Module`
Represents a discrete unit of content within a course.

| Field | Type | Description |
|---|---|---|
| `course` | ForeignKey → Course | Parent course (cascade delete) |
| `title` | CharField | Module name |
| `order` | IntegerField | Position in course sequence |

### `LearningProgress`
Records the relationship between a learner and a completed module.

| Field | Type | Description |
|---|---|---|
| `learner_name` | CharField | Learner identifier |
| `course` | ForeignKey → Course | Enrolled course |
| `completed_modules` | ManyToManyField → Module | Set of completed modules |
| `last_updated` | DateTimeField | Auto-updated on progress save |

The dashboard view derives `completion_percentage` dynamically by comparing the count of a learner's `completed_modules` against the total module count for their enrolled `course`.

---

## Quick Start

### Prerequisites

- Python 3.10+
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Madhumitxx13/lms-track-learning.git
cd lms-track-learning
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate — Linux / macOS
source venv/bin/activate

# Activate — Windows (PowerShell)
venv\Scripts\Activate.ps1

# Activate — Windows (Git Bash)
source venv/Scripts/activate
```

### 3. Install Dependencies

```bash
pip install django
```

> **Note:** A `requirements.txt` is recommended for team use. Generate one with `pip freeze > requirements.txt` after installation.

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create an Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

| URL | Description |
|---|---|
| `http://127.0.0.1:8000/admin/` | Django admin panel — manage courses, modules, and progress records |
| `http://127.0.0.1:8000/dashboard/` | Learner progress analytics dashboard |

---

## Dashboard

The dashboard is the central interface for monitoring learning outcomes. It is served by the `dashboard` view in `lms_core/views.py` and rendered via `templates/dashboard.html`.

### What's Displayed

For every active `LearningProgress` record, the dashboard surfaces:

- **Course Name** — the enrolled course
- **Learner Name** — the individual being tracked
- **Modules Completed** — count of completed modules (e.g., 3 of 5)
- **Progress Bar** — Bootstrap-rendered visual indicator
- **Completion %** — dynamically computed percentage

### Sample Data Flow

```
Admin creates: "Python Fundamentals" (5 modules)
Admin records:  Learner "Madhumitha" completed 3 modules

Dashboard shows:
┌─────────────────────┬───────────────┬──────────┬─────────────────────┬──────┐
│ Course              │ Learner       │ Modules  │ Progress            │    % │
├─────────────────────┼───────────────┼──────────┼─────────────────────┼──────┤
│ Python Fundamentals │ Madhumitha    │  3 / 5   │ ████████░░░░░░░░░░░ │  60% │
└─────────────────────┴───────────────┴──────────┴─────────────────────┴──────┘
```

---

## Admin Panel Guide

Django's built-in admin is pre-configured via `lms_core/admin.py` to manage all three models.

### Workflow

**Step 1 — Create a Course**
`Admin → Courses → Add Course` → Enter title and description → Save.

**Step 2 — Add Modules**
`Admin → Modules → Add Module` → Select parent course, enter title, set order → Save. Repeat for each module.

**Step 3 — Record Learner Progress**
`Admin → Learning Progresses → Add` → Enter learner name, select course, tick completed modules → Save.

**Step 4 — View Dashboard**
Navigate to `http://127.0.0.1:8000/dashboard/` to see all progress records rendered with completion percentages.

---

## Use Cases

The platform is well-suited to any context that requires structured content delivery with measurable outcomes:

- **Corporate Training** — Onboarding programs, compliance training, technical skill development
- **Higher Education** — Course module tracking for universities and colleges
- **Bootcamps & Certification Programs** — Progress monitoring for intensive learning paths
- **Employee Upskilling** — Internal L&D teams tracking skill development against defined curricula
- **Internship Programs** — Tracking intern progress through structured onboarding modules

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | Python 3.10+ / Django 6.0 |
| **Frontend** | HTML5, CSS3, Bootstrap |
| **Database (Dev)** | SQLite3 |
| **Database (Prod-ready)** | PostgreSQL / MySQL (via Django ORM swap) |
| **Authentication** | Django Admin Auth System |
| **ORM** | Django ORM (QuerySet API) |
| **Template Engine** | Django Template Language (DTL) |
| **ASGI/WSGI** | Gunicorn / Uvicorn compatible |
| **Version Control** | Git & GitHub |

---

## Configuration

Key settings live in `lms/settings.py`. For production deployments, the following should be updated:

```python
# Security
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')   # Move to environment variable
DEBUG = False                                        # Disable in production
ALLOWED_HOSTS = ['yourdomain.com']                  # Set your domain

# Database (swap SQLite for PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': '5432',
    }
}

# Static files (for production)
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

---

## Roadmap

Planned enhancements to evolve this into a full-featured enterprise LMS:

| Feature | Status |
|---|---|
| Role-based access control (Student / Trainer / Admin) | 🔜 Planned |
| Learner self-enrollment portal | 🔜 Planned |
| REST API layer (Django REST Framework) | 🔜 Planned |
| Graph-based completion analytics (Chart.js / D3.js) | 🔜 Planned |
| Email notifications on module completion | 🔜 Planned |
| Certificate generation on course completion | 🔜 Planned |
| PostgreSQL / cloud database support | 🔜 Planned |
| Docker containerization | 🔜 Planned |
| Responsive mobile UI | 🔜 Planned |
| Export progress reports as PDF/CSV | 🔜 Planned |

---

## Contributing

Contributions, issues, and feature requests are welcome.

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: describe your change"
git push origin feature/your-feature-name
# Open a Pull Request on GitHub
```

Please follow [PEP 8](https://peps.python.org/pep-0008/) for Python code and keep templates clean and well-commented.


---

<div align="center">

Built by [Madhumitha S](https://github.com/Madhumitxx13)

*Industry-Aligned Learning Management System — Focused on Scalability, Clarity, and Real-World LMS Design*

</div>
