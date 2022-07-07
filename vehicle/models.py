from django.core.validators import MinValueValidator
from django.db import models

from vehicle.helpers import max_value_current_year


class Vehicle(models.Model):
    """ Vehicle """

    mark = models.CharField('mark', max_length=30)
    model = models.CharField('model', max_length=30)
    color = models.CharField('color', max_length=30)
    reg = models.CharField('registration number', unique=True, max_length=30)
    year = models.SmallIntegerField('year', validators=[MinValueValidator(1984), max_value_current_year])
    vin = models.CharField('vin', max_length=30, unique=True)
    vrc = models.CharField('vehicle registration certificate (VRC)', unique=True, max_length=30)
    vrc_date = models.DateField('VRC date', max_length=30)

    class Meta:
        verbose_name_plural = "vehicles"

    def __str__(self):
        return f'{self.mark} {self.model} {self.reg}'
