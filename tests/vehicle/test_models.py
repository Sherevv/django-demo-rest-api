from datetime import date

from django.test import TestCase

from vehicle.models import Vehicle


class VehicleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Vehicle.objects.create(
            mark='BMW',
            model='x5',
            color='black',
            reg='reg_test_number',
            year=2010,
            vin='vin_test_number',
            vrc='vrc_test_number',
            vrc_date=date.today()
        )

    def test_model_labels(self):
        vehicle = Vehicle.objects.get(id=1)
        field_label = vehicle._meta.get_field('mark').verbose_name
        self.assertEquals(field_label, 'mark')

    def test_string_representation(self):
        vehicle = Vehicle.objects.get(id=1)
        expected_object_name = f'{vehicle.mark} {vehicle.model} {vehicle.reg}'
        self.assertEquals(expected_object_name, str(vehicle))

    def test_unique_fields(self):
        vehicle = Vehicle.objects.get(id=1)
        expected_object_name = f'{vehicle.mark} {vehicle.model} {vehicle.reg}'
        self.assertEquals(expected_object_name, str(vehicle))
