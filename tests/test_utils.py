# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest

from centerline.exceptions import InvalidInputTypeError
from centerline.utils import get_ogr_driver


def test__driver_name__with_shp__returns_esri_shapefile(create_input_file):
    EXPECTED_DRIVER_NAME = "ESRI Shapefile"

    input_file = create_input_file("polygons", "shp")
    driver = get_ogr_driver(input_file)

    assert driver.GetName() == EXPECTED_DRIVER_NAME


def test__driver_name__with_json__returns_geojson(create_input_file):
    EXPECTED_DRIVER_NAME = "GeoJSON"
    input_file = "example.json"

    driver = get_ogr_driver(input_file)

    assert driver.GetName() == EXPECTED_DRIVER_NAME


def test__driver_name__with_geojson__returns_geojson(create_input_file):
    EXPECTED_DRIVER_NAME = "GeoJSON"
    input_file = create_input_file("polygons", "geojson")

    driver = get_ogr_driver(input_file)

    assert driver.GetName() == EXPECTED_DRIVER_NAME


def test__with_unknown_extension__returns_valueerror():
    input_file = "example.unknown"

    with pytest.raises(InvalidInputTypeError):
        get_ogr_driver(input_file)
