# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
import os

import click
import fiona

from osgeo import gdal, ogr
from shapely.geometry import mapping, shape

from .exceptions import (
    InvalidInputTypeError,
    TooFewRidgesError,
    UnsupportedVectorType,
)
from .geometry import Centerline


# Enable GDAL/OGR exceptions
gdal.UseExceptions()


@click.command()
@click.argument("src", nargs=1, type=click.Path(exists=True))
@click.argument("dst", nargs=1, type=click.Path(exists=False))
@click.option(
    "--interpolation-distance",
    default=0.5,
    show_default=True,
    help=(
        "Densify the input geometry's border by placing additional "
        "points at this distance"
    ),
)
def create_centerlines(src, dst, interpolation_distance=0.5):
    """Convert the geometries from the ``src`` file to centerlines in
    the ``dst`` file.

    Use the ``interpolation_distance`` parameter to adjust the level of
    detail you want the centerlines to be produced with.

    Only polygons and multipolygons are converted to centerlines,
    whereas the other geometries are skipped. The polygon's attributes
    are copied to its ``Centerline`` object.

    If the ``interpolation_distance`` factor does not suit the polygon's
    geometry, the ``TooFewRidgesError`` error is logged as a warning.
    You should try readjusting the ``interpolation_distance`` factor and
    rerun the command.

    :param src: path to the file containing input geometries
    :type src: str
    :param dst: path to the file that will contain the centerlines
    :type dst: str
    :param interpolation_distance: densify the input geometry's
        border by placing additional points at this distance, defaults
        to 0.5 [meter].
    :type interpolation_distance: float, optional
    :return: ``dst`` file is generated
    :rtype: None
    """

    with fiona.Env():
        with fiona.open(src, mode="r") as source_file:
            schema = source_file.schema.copy()
            schema.update({"geometry": "MultiLineString"})
            driver = get_ogr_driver(filepath=dst)
            with fiona.open(
                dst,
                mode="w",
                driver=driver.GetName(),
                schema=schema,
                crs=source_file.crs,
                encoding=source_file.encoding,
            ) as destination_file:
                for record in source_file:
                    geom = record.get("geometry")
                    input_geom = shape(geom)

                    attributes = record.get("properties")
                    try:
                        centerline_obj = Centerline(
                            input_geom, interpolation_distance, **attributes
                        )
                    except (InvalidInputTypeError, TooFewRidgesError) as error:
                        logging.warning(error)
                        continue

                    centerline_dict = {
                        "geometry": mapping(centerline_obj.geometry),
                        "properties": {
                            k: v
                            for k, v in centerline_obj.__dict__.items()
                            if k in attributes.keys()
                        },
                    }

                    destination_file.write(centerline_dict)

    return None


def get_ogr_driver(filepath):
    """Get the OGR driver based on the file's extension.

    :param filepath: file's path
    :type filepath: str
    :raises UnsupportedVectorType: unsupported extension
    :return: OGR driver
    :rtype: osgeo.ogr.Driver
    """
    filename, file_extension = os.path.splitext(filepath)
    extension = file_extension[1:]

    ogr_driver_count = ogr.GetDriverCount()
    for idx in range(ogr_driver_count):
        driver = ogr.GetDriver(idx)
        driver_extension = driver.GetMetadataItem(str("DMD_EXTENSION")) or ""
        driver_extensions = driver.GetMetadataItem(str("DMD_EXTENSIONS")) or ""

        if extension == driver_extension or extension in driver_extensions:
            return driver

    raise UnsupportedVectorType
