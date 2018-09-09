# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from osgeo import gdal, ogr
from shapely.geometry import MultiPolygon, Polygon

# Enable GDAL/OGR exceptions
gdal.UseExceptions()


ALLOWED_INPUT_GEOMETRIES = ('Polygon', 'MultiPolygon')


def is_valid_geometry(geometry):
    """
    Confirm that the geometry type is of type Polygon or MultiPolygon.

    Args:
        geometry (BaseGeometry): BaseGeometry instance (e.g. Polygon)

    Returns:
        bool

    """
    if isinstance(geometry, Polygon) or isinstance(geometry, MultiPolygon):
        return True
    else:
        return False


def get_ogr_driver(filepath):
    """
    Get the OGR driver from the provided file extension.

    Args:
        file_extension (str): file extension

    Returns:
        osgeo.ogr.Driver

    Raises:
        ValueError: no driver is found

    """
    filename, file_extension = os.path.splitext(filepath)
    EXTENSION = file_extension[1:]

    ogr_driver_count = ogr.GetDriverCount()
    for idx in range(ogr_driver_count):
        driver = ogr.GetDriver(idx)
        driver_extension = driver.GetMetadataItem(str('DMD_EXTENSION')) or ''
        driver_extensions = driver.GetMetadataItem(str('DMD_EXTENSIONS')) or ''

        if EXTENSION == driver_extension or EXTENSION in driver_extensions:
            return driver

    else:
        msg = 'No driver found for the following file extension: {}'.format(
            EXTENSION)
        raise ValueError(msg)
