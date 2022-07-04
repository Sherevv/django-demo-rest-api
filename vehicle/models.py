import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Vehicle(models.Model):
    mark = models.CharField('марка', max_length=30)
    model = models.CharField('модель', max_length=30)
    color = models.CharField('цвет', max_length=30)
    reg = models.CharField('регистрационный номер', unique=True, max_length=30)
    year = models.SmallIntegerField('год выпуска', validators=[MinValueValidator(1984),
                                                               max_value_current_year])
    vin = models.CharField('vin', max_length=30, unique=True)
    vrc = models.CharField('номер СТС (свидетельство о регистрации)', unique=True, max_length=30)
    vrc_date = models.DateField('дата СТС', max_length=30)

    class Meta:
        verbose_name = 'транспортное средство'
        verbose_name_plural = "транспортные средства"
