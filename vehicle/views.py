from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, JsonResponse
from tablib import Dataset
from rest_framework import status

from vehicle.resources import VehicleResource


def export_resource(request, file_format, resource):
    dataset = resource.export()

    if file_format == 'xls':
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="export_data.xls"'
    elif file_format == 'csv':
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export_data.csv"'
    else:
        response = JsonResponse({'error': 'Wrong export format, allowed: csv, xls'},
                                status=status.HTTP_400_BAD_REQUEST)
    return response


@login_required
@permission_required('vehicle.view_vehicle')
def export_vehicle(request, format):
    return export_resource(request, format, VehicleResource())


def import_resource(request, file_format, resource):
    dataset = Dataset()
    import_data = request.FILES.get('importData')
    if not import_data:
        return JsonResponse({'error': 'Import error: file did not send'},
                            status=status.HTTP_400_BAD_REQUEST)

    if file_format == 'csv':
        imported_data = dataset.load(import_data.read().decode('utf-8'), format='csv')
        result = resource.import_data(dataset, dry_run=True)
    elif file_format == 'xls':
        imported_data = dataset.load(import_data.read().decode('utf-8'), format='xls')
        result = resource.import_data(dataset, dry_run=True)
    else:
        return JsonResponse({'error': 'Wrong import format, allowed: csv, xls'},
                            status=status.HTTP_400_BAD_REQUEST)

    if not result.has_errors():
        resource.import_data(dataset, dry_run=False)
        return JsonResponse({'message': 'success'})
    else:
        errors = []
        for i, v in result.row_errors():
            for v2 in v:
                errors.append({'error': str(v2.error), 'row': v2.row})
        return JsonResponse({'errors': errors},
                            status=status.HTTP_400_BAD_REQUEST)


@login_required
@permission_required('vehicle.add_vehicle')
def import_vehicle(request, format):
    if request.method == 'POST':
        return import_resource(request, format, VehicleResource())
    else:
        return JsonResponse({'error': 'Request should be POST'},
                            status=status.HTTP_400_BAD_REQUEST)
