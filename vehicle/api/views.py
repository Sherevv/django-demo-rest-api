from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from vehicle.api.serializers import VehicleSerializer
from vehicle.models import Vehicle


class ActualDjangoModelPermissions(permissions.DjangoModelPermissions):
    view_permissions = ['%(app_label)s.view_%(model_name)s']

    perms_map = {
        'GET': view_permissions,
        'OPTIONS': view_permissions,
        'HEAD': view_permissions,
        'POST': permissions.DjangoModelPermissions.perms_map['POST'],
        'PUT': permissions.DjangoModelPermissions.perms_map['PUT'],
        'PATCH': permissions.DjangoModelPermissions.perms_map['PATCH'],
        'DELETE': permissions.DjangoModelPermissions.perms_map['DELETE'],
    }


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated, ActualDjangoModelPermissions]
    filterset_fields = ['mark', 'model', 'color', 'reg', 'year', 'vin', 'vrc', 'vrc_date']
