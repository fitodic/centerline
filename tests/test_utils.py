# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from unittest import TestCase

from centerline.utils import get_ogr_driver


class TestGetOgrDriver(TestCase):

    def test__driver_name__with_shp__returns_esri_shapefile(self):
        FILE_EXTENSION = 'shp'
        EXPECTED_DRIVER_NAME = 'ESRI Shapefile'

        driver = get_ogr_driver(FILE_EXTENSION)

        self.assertEqual(driver.GetName(), EXPECTED_DRIVER_NAME)

    def test__driver_name__with_json__returns_geojson(self):
        FILE_EXTENSION = 'json'
        EXPECTED_DRIVER_NAME = 'GeoJSON'

        driver = get_ogr_driver(FILE_EXTENSION)

        self.assertEqual(driver.GetName(), EXPECTED_DRIVER_NAME)

    def test__driver_name__with_geojson__returns_geojson(self):
        FILE_EXTENSION = 'geojson'
        EXPECTED_DRIVER_NAME = 'GeoJSON'

        driver = get_ogr_driver(FILE_EXTENSION)

        self.assertEqual(driver.GetName(), EXPECTED_DRIVER_NAME)

    def test__with_unknown_extension__returns_valueerror(self):
        FILE_EXTENSION = 'unknown'

        with self.assertRaises(ValueError):
            get_ogr_driver(FILE_EXTENSION)
