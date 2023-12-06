from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import BeiJiang,BridageImage
# Register your models here.


class BeiJiangAdmin(LeafletGeoAdmin):
    pass


class BridageImageAdmin(LeafletGeoAdmin):
    pass

admin.site.register(BeiJiang,BeiJiangAdmin)
admin.site.register(BridageImage,BridageImageAdmin)