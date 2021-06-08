from django.urls import path
from .views import Lesson
from quiz.views import Quiz
app_name = 'lesson'

urlpatterns = [
    path('', Lesson.as_view(),name='lesson'),
    path('r/<str:topic>/', Quiz.as_view(), name='quiz'),
]
