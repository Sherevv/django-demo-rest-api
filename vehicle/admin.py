from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from vehicle.models import Vehicle
from vehicle.resources import VehicleResource


class VehicleAdmin(ImportExportModelAdmin):
    resource_class = VehicleResource


admin.site.register(Vehicle, VehicleAdmin)
