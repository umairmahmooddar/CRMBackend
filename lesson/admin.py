from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]