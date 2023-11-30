## version 0.0.1

# 一、 geoshare 基本功能
geodjango + leaflet 

# 二、环境配置

**git问题** ：Failed to connect to github.com port 443:connection timed out 。

##### 解决办法：取消全局代理，如下：
    
    git config --global --unset http.proxy 
    git config --global --unset https.prox

**pip更新后出现no module named pip 问题**:运行一下代码：
    python -m ensurepip

#### 环境配置配置
>配置项目所需库及注意事项

虚拟环境配置

    #安装虚拟环境创建库
    pip install virtualenv
    pip install virtualenvwrapper-win #linux 安装使用:pip install virtualenvwrapper
- window配置：

>1、打开控制面板-系统和安全-系统-高级系统设置-环境变量-系统变量-点击新建  
2、变量名：输入 WORKON_HOME， 变量值：输入自定义的路径，确定保存即可。  
3、进入pthon的安装路径，我这里是C:\Program Files\python36\Scripts下，具体根据自己的安装路径双击virtualenvwrapper.bat 。  
4、然后重新打开cmd即可使用
- LINUX 配置：
> 编辑 shell 的 RC 文件（例如 .bashrc、.bash_profile 或 .zshrc）并添加以下几行：

    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
    source /usr/local/bin/virtualenvwrapper.sh


创建虚拟环境: mkvirtualenv [环境名称]  
运行环境：    workon [环境名称]  
退出环境： deactivate  
删除环境：rmvirtualenv [环境名称]  

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


[VSCode安装Django插件后实现html语法提示的两个方法及操作步骤](https://www.cainiaoxueyuan.com/office/28106.html)

[bootstrap文档](https://v5.bootcss.com/docs/getting-started/introduction/)


### 静态文件设置
    #setting.py中添加
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [
    BASE_DIR / "static"]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    
    #在urls.py中设置
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


### [geodjango配置](https://www.pointsnorthgis.ca/blog/geodjango-gdal-setup-windows-10/)


    pipwin install gdal



    if os.name == 'nt':
        VIRTUAL_ENV_BASE = os.environ['VIRTUAL_ENV']
        os.environ['PATH'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
        os.environ['PROJ_LIB'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']
