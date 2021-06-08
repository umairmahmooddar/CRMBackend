from django.db import models

# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length=500,default='')
    videoURL = models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.name