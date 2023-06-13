from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    profile = models.ImageField(upload_to='static/img/')
    client_name = models.CharField(max_length=10)
    real_name = models.CharField(max_length=10)