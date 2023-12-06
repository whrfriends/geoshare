from django.db import models

# Create your models here.
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class BeiJiang(models.Model):
    name = models.CharField(max_length=254)
    descriptio = models.CharField(max_length=254,null=True)
    timestamp = models.CharField(max_length=24,null=True)
    begin = models.CharField(max_length=24,null=True)
    end = models.CharField(max_length=24,null=True)
    altitudemo = models.CharField(max_length=254,null=True)
    tessellate = models.BigIntegerField(null=True)
    extrude = models.BigIntegerField(null=True)
    visibility = models.BigIntegerField(null=True)
    draworder = models.BigIntegerField(null=True)
    icon = models.CharField(max_length=254,null=True)
    fid = models.FloatField(null=True)
    墩号 = models.BigIntegerField(null=True)
    geom = models.MultiPointField(srid=4326)

class BridageImage(models.Model):
    name = models.CharField( max_length=50)
    beijiang = models.ForeignKey(BeiJiang,on_delete=models.CASCADE)
