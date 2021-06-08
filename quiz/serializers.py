from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Quizzes, Question, Answer

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id',
            'answerBody',
            'isCorrect',
        ]

class QuestionsSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many = True, read_only = True)
    quiz = QuizSerializer(read_only = True)
    
    class Meta:
        model = Question
        fields = [
            'quiz',
            'title',
            'answer',
        ]