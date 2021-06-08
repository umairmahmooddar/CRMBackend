from django.contrib import admin
from . import models
from lesson.admin import LessonAdmin
# Register your models here.


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]
class AnswerInLineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answerBody',
        'isCorrect',
    ]
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
        'dateCreated',
    ]
    inlines = [
        AnswerInLineModel,
    ]

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answerBody',
        'isCorrect',
        'question',
    ]