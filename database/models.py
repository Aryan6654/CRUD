from datetime import datetime
from django.db import models

# Create your models here.
class addUser(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.DateField()
