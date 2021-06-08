from django.urls import path
from .views import Questions

app_name = 'quiz'

urlpatterns = [
    # path('', Quizzes.as_view(), name='quiz'),
    path('r/<str:topic>/', Questions.as_view(), name='question'),
]
