## version 0.0.1

# 一、 geohares 基本功能
geodjango + leaflet 

# 二、环境配置

**git问题** ：Failed to connect to github.com port 443:connection timed out 。

##### 解决办法：取消全局代理，如下：
    
    git config --global --unset http.proxy 
    git config --global --unset https.prox


#### django库安装、配置
>配置项目所需库及注意事项

- [rest_framework安装](https://www.django-rest-framework.org/)
```
    pip install djangorestframework # restframework
    pip install markdown       
    pip install django-filter


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
```

