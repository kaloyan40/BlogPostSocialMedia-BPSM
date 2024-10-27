import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("Паролата трябва да има поне една цифра, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Паролата трябва да има поне една цифра, 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("Паролата трябва да има поне една главна буква, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Паролата трябва да има поне една главна буква, A-Z."
        )
