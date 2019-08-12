from django.db import models

class Job(models.Model):
    images = models.ImageField(upload_to='media/')
    summary = models.CharField(max_length=200)
