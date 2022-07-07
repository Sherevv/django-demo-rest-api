from import_export.resources import ModelResource
from tablib import Dataset

from django.http import HttpResponse, JsonResponse, HttpRequest
from rest_framework import status

from .models import Vehicle


class VehicleResource(ModelResource):
    class Meta:
        model = Vehicle


def export_resource(request: HttpRequest, file_format: str, resource: ModelResource) -> HttpResponse:
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


def import_resource(request: HttpRequest, file_format: str, resource: ModelResource) -> JsonResponse:
    dataset = Dataset()
    import_data = request.FILES.get('importData')
    if not import_data:
        return JsonResponse({'error': 'Import error: file did not send'},
                            status=status.HTTP_400_BAD_REQUEST)

    if file_format == 'csv':
        dataset.load(import_data.read().decode('utf-8'), format='csv')
        result = resource.import_data(dataset, dry_run=True)
    elif file_format == 'xls':
        dataset.load(import_data.read().decode('utf-8'), format='xls')
        result = resource.import_data(dataset, dry_run=True)
    else:
        return JsonResponse({'error': 'Wrong import format, allowed: csv, xls'},
                            status=status.HTTP_400_BAD_REQUEST)

    if not result.has_errors():
        resource.import_data(dataset, dry_run=False)
        return JsonResponse({'message': 'success'})
    else:
        errors = []
        for _, v in result.row_errors():
            for v2 in v:
                errors.append({'error': str(v2.error), 'row': v2.row})

        return JsonResponse({'errors': errors},
                            status=status.HTTP_400_BAD_REQUEST)
