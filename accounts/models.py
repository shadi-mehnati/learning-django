from django.db import models

# Create your models here.
class logins(models.Model):
    userId=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=15)
    email=models.TextField(max_length=170)