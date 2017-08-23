# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from osgeo import gdal, ogr

# Enable GDAL/OGR exceptions
gdal.UseExceptions()


def get_ogr_driver(file_extension):
    """Get the OGR driver from the provided file extension.

    Args:
        file_extension {str}: file extension

    Returns:
        {osgeo.ogr.Driver}

    Raises:
        {ValueError}: when no driver is found

    """
    ogr_driver_count = ogr.GetDriverCount()
    for idx in range(ogr_driver_count):
        driver = ogr.GetDriver(idx)
        driver_extension = driver.GetMetadataItem(str('DMD_EXTENSION')) or ''
        driver_extensions = driver.GetMetadataItem(str('DMD_EXTENSIONS')) or ''

        if (file_extension == driver_extension or
                file_extension in driver_extensions):
            return driver

    else:
        msg = 'No driver found for the following file extension: {}'.format(
            file_extension)
        raise ValueError(msg)


def get_polygon_features(filepath):
    """Get the Polygon or MultiPolygon features from the source file.

    Args:
        filepath {str}: path to the source file

    Yields:
        {osgeo.ogr.Feature}: a Polygon or a MultiPolygon feature

    Raises:
        {AttributeError}: invalid filepath
        {ValueError}: no driver is found

    """
    filename, file_extension = os.path.splitext(filepath)

    try:
        driver = get_ogr_driver(file_extension=file_extension[1:])
    except ValueError:
        raise

    datasource = driver.Open(filepath, 0)

    try:
        layer_count = datasource.GetLayerCount()
    except AttributeError:
        raise

    for layer_idx in range(layer_count):
        layer = datasource.GetLayerByIndex(layer_idx)
        layer_geometry_type = layer.GetGeomType()

        if layer_geometry_type == ogr.wkbPolygon:
            feature = layer.GetNextFeature()
            while feature is not None:
                yield feature
                feature = layer.GetNextFeature()

    datasource.Destroy()
