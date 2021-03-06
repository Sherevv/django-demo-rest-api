# Generated by Django 4.0.5 on 2022-07-04 08:50

import django.core.validators
from django.db import migrations, models
import vehicle.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=30, verbose_name='марка')),
                ('model', models.CharField(max_length=30, verbose_name='модель')),
                ('color', models.CharField(max_length=30, verbose_name='цвет')),
                ('reg', models.CharField(max_length=30, unique=True, verbose_name='регистрационный номер')),
                ('year', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1984), vehicle.models.max_value_current_year], verbose_name='год выпуска')),
                ('vin', models.CharField(max_length=30, unique=True, verbose_name='vin')),
                ('vrc', models.CharField(max_length=30, unique=True, verbose_name='номер СТС (свидетельство о регистрации)')),
                ('vrc_date', models.DateField(max_length=30, verbose_name='дата СТС')),
            ],
            options={
                'verbose_name': 'транспортное средство',
                'verbose_name_plural': 'транспортные средства',
            },
        ),
    ]
