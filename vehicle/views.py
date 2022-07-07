from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, JsonResponse, HttpRequest

from rest_framework import status

from vehicle.resources import VehicleResource, export_resource, import_resource


@permission_required('vehicle.view_vehicle')
def export_vehicle(request: HttpRequest, ext: str) -> HttpResponse:
    return export_resource(ext, VehicleResource())


@permission_required('vehicle.add_vehicle')
def import_vehicle(request: HttpRequest, ext: str) -> JsonResponse:
    if request.method == 'POST':
        return import_resource(request, ext, VehicleResource())
    else:
        return JsonResponse({'error': 'Request should be POST'},
                            status=status.HTTP_400_BAD_REQUEST)
