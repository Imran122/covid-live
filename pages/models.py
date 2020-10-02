from django.db import models
from datetime import datetime 
# Create your models here.
class Symptoms(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=50, null=True)
    temperature = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    score = models.IntegerField(null=True)
    result = models.CharField(max_length=200,null=True)

    

    def __str__(self):
        return self.name