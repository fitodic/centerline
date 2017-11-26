# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from unittest import TestCase

from centerline.utils import get_ogr_driver, is_polygon

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
SHP_DIR = os.path.join(TESTS_DIR, 'data', 'shp')
GEOJSON_DIR = os.path.join(TESTS_DIR, 'data', 'geojson')


class TestIsPolygon(TestCase):

    def test__returns_true(self):
        self.assertTrue(is_polygon('Polygon'))

    def test__returns_false_for_multipolygon(self):
        self.assertFalse(is_polygon('MultiPolygon'))


class TestGetOgrDriver(TestCase):

    def test__driver_name__with_shp__returns_esri_shapefile(self):
        FILE_EXTENSION = 'example.shp'
        EXPECTED_DRIVER_NAME = 'ESRI Shapefile'

        driver = get_ogr_driver(FILE_EXTENSION)

        self.assertEqual(driver.GetName(), EXPECTED_DRIVER_NAME)

    def test__driver_name__with_json__returns_geojson(self):
        FILE_EXTENSION = 'example.json'
        EXPECTED_DRIVER_NAME = 'GeoJSON'

        driver = get_ogr_driver(FILE_EXTENSION)

        self.assertEqual(driver.GetName(), EXPECTED_DRIVER_NAME)

    def test__driver_name__with_geojson__returns_geojson(self):
        FILE_EXTENSION = 'example.geojson'
        EXPECTED_DRIVER_NAME = 'GeoJSON'

        driver = get_ogr_driver(FILE_EXTENSION)

        self.assertEqual(driver.GetName(), EXPECTED_DRIVER_NAME)

    def test__with_unknown_extension__returns_valueerror(self):
        FILE_EXTENSION = 'example.unknown'

        with self.assertRaises(ValueError):
            get_ogr_driver(FILE_EXTENSION)
