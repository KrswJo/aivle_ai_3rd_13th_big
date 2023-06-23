from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_card_validity_period(value):
    # 입력된 값이 YYYY MM 형식인지 확인
    pattern = r'^\d{4} \d{2}$'
    if not re.match(pattern, value):
        raise ValidationError('Card validity period should be in YYYY MM format.')


class User(AbstractUser):
    nickname = models.CharField(max_length=15, unique=True, null=True)
    costco_id = models.CharField(max_length=15, unique=True, null=True)
    english_name = models.CharField(max_length=15, unique=False, null=True)
    card_validity_period = models.CharField(
        max_length=7,
        validators=[
            RegexValidator(
                regex=r'^\d{4} \d{2}$',
                message='정확한 날짜를 입력해 주세요.',
            ),
            validate_card_validity_period,
        ],
        null=True
    )