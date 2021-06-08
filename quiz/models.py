from django.db import models
from lesson.models import Lesson

# Create your models here.


class Quizzes(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quizzes,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.DO_NOTHING)
    answerBody = models.CharField(max_length=250, default='')
    isCorrect = models.BooleanField(default=False)


    def __str__(self):
        return self.answerBody