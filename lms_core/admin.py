from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Module, LearningProgress

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(LearningProgress)
