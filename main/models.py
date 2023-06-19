from django.db import models

# Create your models here.

# 현재 안쓰는 모델인듯하니 나중에 다시 확인하고 삭제
class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    profile = models.ImageField(upload_to='static/img/')
    client_name = models.CharField(max_length=10)
    real_name = models.CharField(max_length=10)