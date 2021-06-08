from django.http import response
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Answer, Question, Quizzes
from .serializers import QuizSerializer, QuestionsSerializer
# Create your views here.

""" 
class Quizzes(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()
 """

class Quiz(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Quizzes.objects.filter(lesson__name = kwargs['topic']).order_by('?')
        serializer = QuizSerializer(quiz, many = True)
        return Response(serializer.data)

class Questions(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title = kwargs['topic']).order_by('?')
        serializer = QuestionsSerializer(question, many = True)
        return Response(serializer.data)