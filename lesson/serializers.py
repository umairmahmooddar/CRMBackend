from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = [
            'name',
            'intro',
            'videoURL',
        ]