from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=15, unique=True, null=True, default='admin')
    # country = models.CharField(max_length=100, unique=False, null=True)