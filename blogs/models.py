from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=800)
    image = models.ImageField(upload_to='media/')
