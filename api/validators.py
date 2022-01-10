from django.utils import timezone
from django.core.exceptions import ValidationError


def year_validator(value):
    if value < 1900 or value > timezone.now().year:
        raise ValidationError(
            ('%(value)s is not a correcrt year!'),
            params={'value': value},
        )


def validate_score(score):
    if score < 1 or score > 10:
        raise ValidationError('Оценка должна быть в диапазоне от 1 до 10')
