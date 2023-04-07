from django.db import models

# Create your models here.
class quiz(models.Model):
    questions = models.CharField(max_length=20,unique=True)
    answer = models.CharField(max_length=20,unique=True)
    mark = models.CharField(max_length=20,unique=True)
    
    def __str__(self):
        return self.questions

