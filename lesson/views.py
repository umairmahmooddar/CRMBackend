from django.shortcuts import render
from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer
# Create your views here.


class Lesson(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()