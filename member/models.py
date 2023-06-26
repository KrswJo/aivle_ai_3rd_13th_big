from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import datetime

def validate_card_validity_period(value):
    current_server_time = datetime.now()
    current_request_time = datetime.strptime(value, "%Y-%m")
    if current_request_time.year < current_server_time.year or current_request_time.month < current_server_time.month :
        raise ValidationError('카드 유효기간이 올바르지 못합니다.')


class User(AbstractUser):
    nickname = models.CharField(max_length=15, unique=True, null=True)
    costco_id = models.CharField(max_length=15, unique=True, null=True)
    english_name = models.CharField(max_length=15, unique=False, null=True)
    card_validity_period = models.CharField(
        max_length=15,
        validators=[
            validate_card_validity_period,
        ],
        null=True
    )