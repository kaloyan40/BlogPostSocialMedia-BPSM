from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.html import strip_tags


def validate_name_len(value):
    if len(value) < 2:
        raise ValidationError(
            _(f"Името не може да е по-малко от 2 символа ('{value}' е {len(value)})"),
            params={"value": value},
        )


def validate_description_len(value):
    if len(strip_tags(value)) < 15:
        raise ValidationError(
            _(f"Описанието не може да е по-малко от 15 символа ('{value}' е {len(strip_tags(value))})"),
            params={"value": value},
        )
