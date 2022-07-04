# Django demo REST api

## Login
Path: `/api-auth/login/`

Login: `admin`, password: `admin`

To test permission use `demo:demo1234`.
`demo` user can only view Vehicle model.

## Search
Based on [django-filter](https://django-filter.readthedocs.io/en/stable/guide/usage.html). 

For search use query params:

`/api/vehicles/?mark=&model=&color=&reg=&year=&vin=&vrc=&vrc_date=`

Example for searching BMW:

`/api/vehicles/?mark=BMW`

## Export-Import
Based on [django-import-export](https://django-import-export.readthedocs.io/en/latest/).

Export path: 
`/api/vehicles/export/csv/` or 
`/api/vehicles/export/xls/`
Import path:
`/api/vehicles/import/csv/` or
`/api/vehicles/import/xls/`