# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from unittest import TestCase

from shapely import geometry

from centerline.utils import get_ogr_driver, is_valid_geometry

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
SHP_DIR = os.path.join(TESTS_DIR, 'data', 'shp')
GEOJSON_DIR = os.path.join(TESTS_DIR, 'data', 'geojson')


class TestIsValidGeometry(TestCase):

    def test_point_returns_false(self):
        self.assertFalse(is_valid_geometry(geometry.Point()))

    def test_multipoint_returns_false(self):
        self.assertFalse(is_valid_geometry(geometry.MultiPoint()))

    def test_linestring_returns_false(self):
        self.assertFalse(is_valid_geometry(geometry.LineString()))

    def test_multilinestring_returns_false(self):
        self.assertFalse(is_valid_geometry(geometry.MultiLineString()))

    def test_linearring_returns_false(self):
        self.assertFalse(is_valid_geometry(geometry.LinearRing()))

    def test_polygon_returns_true(self):
        self.assertTrue(is_valid_geometry(geometry.Polygon()))

    def test_multipolygon_returns_true(self):
        self.assertTrue(is_valid_geometry(geometry.MultiPolygon()))


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
