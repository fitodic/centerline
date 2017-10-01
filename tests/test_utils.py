# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from unittest import TestCase

from centerline.utils import get_ogr_driver, get_polygon_features
from osgeo import ogr

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
SHP_DIR = os.path.join(TESTS_DIR, 'data', 'shp')
GEOJSON_DIR = os.path.join(TESTS_DIR, 'data', 'geojson')


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


class TestGetPolygonFeature(TestCase):

    def test__shp__polygons__feature_count(self):
        EXPECTED_FEATURE_COUNT = 3

        FILEPATH = os.path.join(SHP_DIR, 'polygons.shp')

        features = [feature for feature in get_polygon_features(FILEPATH)]

        self.assertEqual(len(features), EXPECTED_FEATURE_COUNT)

    def test__shp__polygons__feature_type__returns_ogr_feature(self):
        FILEPATH = os.path.join(SHP_DIR, 'polygons.shp')

        for feature in get_polygon_features(FILEPATH):
            self.assertIsInstance(feature, ogr.Feature)

    def test__geojson__polygons__feature_count(self):
        EXPECTED_FEATURE_COUNT = 3

        FILEPATH = os.path.join(GEOJSON_DIR, 'polygons.geojson')

        features = [feature for feature in get_polygon_features(FILEPATH)]

        self.assertEqual(len(features), EXPECTED_FEATURE_COUNT)

    def test__geojson__polygons__feature_type__returns_ogr_feature(self):
        FILEPATH = os.path.join(SHP_DIR, 'polygons.shp')

        for feature in get_polygon_features(FILEPATH):
            self.assertIsInstance(feature, ogr.Feature)

    def test__geojson__linestrings__feature_count(self):
        EXPECTED_FEATURE_COUNT = 0

        FILEPATH = os.path.join(GEOJSON_DIR, 'linestrings.geojson')

        features = [feature for feature in get_polygon_features(FILEPATH)]

        self.assertEqual(len(features), EXPECTED_FEATURE_COUNT)

    def test__geojson__points__feature_count(self):
        EXPECTED_FEATURE_COUNT = 0

        FILEPATH = os.path.join(GEOJSON_DIR, 'points.geojson')

        features = [feature for feature in get_polygon_features(FILEPATH)]

        self.assertEqual(len(features), EXPECTED_FEATURE_COUNT)

    def test__nonexistent_file_with_valid_extension(self):
        FILEPATH = os.path.join(GEOJSON_DIR, 'nonexistent.geojson')

        with self.assertRaises(AttributeError):
            [feature for feature in get_polygon_features(FILEPATH)]

    def test__file_with_an_invalid_extension(self):
        FILEPATH = os.path.join(GEOJSON_DIR, 'nonexistent.invalid')

        with self.assertRaises(ValueError):
            [feature for feature in get_polygon_features(FILEPATH)]
