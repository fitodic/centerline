# -*- coding: utf-8 -*-

from __future__ import unicode_literals

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

