from django.shortcuts import render
from .models import Course, Module, LearningProgress

def dashboard(request):
    data = LearningProgress.objects.select_related('course', 'user')

    total_courses = Course.objects.count()
    total_modules = Module.objects.count()
    completed_modules = sum(item.completed_modules for item in data)

    avg_progress = 0
    if total_modules > 0:
        avg_progress = int((completed_modules / total_modules) * 100)

    context = {
        'data': data,
        'total_courses': total_courses,
        'total_modules': total_modules,
        'completed_modules': completed_modules,
        'avg_progress': avg_progress,
    }

    return render(request, 'dashboard.html', context)
