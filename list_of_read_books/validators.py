from django.core.exceptions import ValidationError

valid_choices = ['read', 'want to read', 'currently reading', 'rereading']


def validation_of_status(value):
    if value not in valid_choices:
        raise ValidationError(f"{value} is not valid")



