import datetime
from django.core.validators import MaxValueValidator


def current_year() -> int:
    return datetime.date.today().year


def max_value_current_year(value: int) -> MaxValueValidator:
    return MaxValueValidator(current_year())(value)
