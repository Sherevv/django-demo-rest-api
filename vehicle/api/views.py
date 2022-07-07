from rest_framework import viewsets

from vehicle.api.serializers import VehicleSerializer
from vehicle.models import Vehicle


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filterset_fields = ['mark', 'model', 'color', 'reg', 'year', 'vin', 'vrc', 'vrc_date']
