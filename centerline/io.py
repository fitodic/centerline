# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import fiona
from shapely.geometry import mapping, shape

from .main import Centerline

ALLOWED_INPUT_GEOMETRY = 'Polygon'


def _is_illegal_geometry(geometry_type):
    if geometry_type != ALLOWED_INPUT_GEOMETRY:
        return True
    else:
        return False


def centerline_shp(src, dst, density=0.5):
    """Create centerlines and save the to an ESRI Shapefile.

    Reads polygons from the `src` ESRI Shapefile, creates Centerline
    objects with the specified `density` parameter and writes them to
    the `dst` ESRI Shapefile.

    Only Polygon features are converted to centerlines. Features of
    different types are skipped.

    Args:
        src (str): source ESRI Shapefile
        dst (str): destination ESRI Shapefile
        density (:obj:`float`, optional): the Centerline's density.
            Defaults to 0.5 (meters)

    Returns:
        None

    """
    with fiona.drivers():
        with fiona.open(path=src, mode='r') as source:
            SCHEMA = source.schema.copy()
            SCHEMA.update({'geometry': 'MultiLineString'})
            with fiona.open(
                    path=dst,
                    mode='w',
                    driver=source.driver,
                    schema=SCHEMA,
                    crs=source.crs,
                    encoding=source.encoding) as destination:
                for record in source:
                    geom = record.get('geometry')

                    # Skip geometries that are not of type Polygon
                    if _is_illegal_geometry(geometry_type=geom.get('type')):
                        continue

                    input_geom = shape(geom)
                    attributes = record.get('properties')
                    centerline_obj = Centerline(
                        input_geom=input_geom,
                        interpolation_dist=density,
                        **attributes
                    )

                    centerline = {}
                    centerline['geometry'] = mapping(centerline_obj)
                    centerline['properties'] = {
                        k: v
                        for k, v in centerline_obj.__dict__.items()
                        if k in attributes.keys()
                    }
                    destination.write(centerline)

    return None
