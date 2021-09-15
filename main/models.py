from django.db import models

from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    biograph = models.TextField()
    created = models.DateTimeField(datetime.today())