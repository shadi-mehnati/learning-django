from django.db import models

# Create your models here.
class Category(models.Model):
    size = models.IntegerField()
    stock = models.IntegerField()
    color = models.TextField(max_length=100)

class products(models.Model):
    name=models.CharField(max_length=200)
    customer=models.ForeignKey("accounts.logins",on_delete=models.CASCADE)

