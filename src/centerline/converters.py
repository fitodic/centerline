# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
import os

import fiona
from osgeo import gdal, ogr
from shapely.geometry import mapping, shape

from .exceptions import InvalidInputTypeError, TooFewRidgesError
from .geometry import Centerline

# Enable GDAL/OGR exceptions
gdal.UseExceptions()


def create_centerlines(src, dst, density=0.5):
    """
    Create centerlines and save the to an ESRI Shapefile.

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
    DST_DRIVER = get_ogr_driver(filepath=dst)

    with fiona.Env():
        with fiona.open(src, mode="r") as source:
            SCHEMA = source.schema.copy()
            SCHEMA.update({"geometry": "MultiLineString"})
            with fiona.open(
                dst,
                mode="w",
                driver=DST_DRIVER.GetName(),
                schema=SCHEMA,
                crs=source.crs,
                encoding=source.encoding,
            ) as destination:
                for record in source:
                    geom = record.get("geometry")
                    input_geom = shape(geom)

                    attributes = record.get("properties")
                    try:
                        centerline_obj = Centerline(
                            input_geom=input_geom,
                            interpolation_dist=density,
                            **attributes
                        )
                    except (InvalidInputTypeError, TooFewRidgesError) as error:
                        logging.warning(error)
                        continue

                    centerline_dict = {
                        "geometry": mapping(centerline_obj),
                        "properties": {
                            k: v
                            for k, v in centerline_obj.__dict__.items()
                            if k in attributes.keys()
                        },
                    }

                    destination.write(centerline_dict)

    return None


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
        driver_extension = driver.GetMetadataItem(str("DMD_EXTENSION")) or ""
        driver_extensions = driver.GetMetadataItem(str("DMD_EXTENSIONS")) or ""

        if EXTENSION == driver_extension or EXTENSION in driver_extensions:
            return driver

    else:
        msg = "No driver found for the following file extension: {}".format(
            EXTENSION
        )
        raise InvalidInputTypeError(msg)
