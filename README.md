# geoshare
geodjango + leaflet 

### 0.0.1 version
    1、add requrements.



pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support


INSTALLED_APPS = [
    ...
    'rest_framework',
]

urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
