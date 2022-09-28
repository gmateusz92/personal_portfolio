from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    descr = models.CharField(max_length=100)
