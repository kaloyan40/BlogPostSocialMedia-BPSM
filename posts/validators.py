from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_len(value):
    if len(value) < 3:
        raise ValidationError(
            _(f"Не може да е по-малко от 3 символа ('{value}' е {len(value)})"),
            params={"value": value},
        )
