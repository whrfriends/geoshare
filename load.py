from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from api.models import BeiJiang

# Auto-generated `LayerMapping` dictionary for BeiJiang model
beijiang_mapping = {
    'name': 'Name',
    'descriptio': 'descriptio',
    'timestamp': 'timestamp',
    'begin': 'begin',
    'end': 'end',
    'altitudemo': 'altitudeMo',
    'tessellate': 'tessellate',
    'extrude': 'extrude',
    'visibility': 'visibility',
    'draworder': 'drawOrder',
    'icon': 'icon',
    'fid': 'fid',
    '墩号': '墩号',
    'geom': 'MULTIPOINT',
}

beijiang_shp = Path(__file__).resolve().parent / 'static/data' / '北江.shp'

def run(verbose=True):
    lm = LayerMapping(BeiJiang, beijiang_shp, beijiang_mapping, transform=False,encoding='utf-8')
    lm.save(strict=True, verbose=verbose)