# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
import os
import shutil
from unittest import TestCase

import fiona

from centerline.io import create_centerlines

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_DIR = os.path.join(TESTS_DIR, 'tmp')
SHP_DIR = os.path.join(TESTS_DIR, 'data', 'shp')
GEOJSON_DIR = os.path.join(TESTS_DIR, 'data', 'geojson')


class TestCreateCenterlines(TestCase):

    def setUp(self):
        self.INPUT_SHP = os.path.join(SHP_DIR, 'polygons.shp')
        os.mkdir(TMP_DIR)

    def tearDown(self):
        if os.path.exists(TMP_DIR):
            shutil.rmtree(TMP_DIR)

    def test__shp_to_shp_execution_successful_returns_None(self):
        DST_SHP = os.path.join(TMP_DIR, 'centerlines.shp')

        output = create_centerlines(src=self.INPUT_SHP, dst=DST_SHP)
        self.assertIsNone(output)

    def test__shp_to_shp_too_big_density(self):
        DST_SHP = os.path.join(TMP_DIR, 'centerlines.shp')
        saved_rows = []

        def fake_warning(s, arg=None):
            if arg is not None:
                s = s % arg
            saved_rows.append(s)

        orig_warning = logging.warning
        logging.warning = fake_warning
        create_centerlines(src=self.INPUT_SHP, dst=DST_SHP, density=11)
        self.assertEqual(
            saved_rows[0],
            "ignoring record that could not be processed: " +
            "Number of produced ridges is too small: " +
            "0, this might be caused by too large " +
            "interpolation distance.",
        )
        logging.warning = orig_warning

    def test__shp_to_shp_records_geom_type_is_multilinestring(self):
        EXPECTED_TYPE = 'MultiLineString'

        DST_SHP = os.path.join(TMP_DIR, 'centerlines.shp')
        create_centerlines(src=self.INPUT_SHP, dst=DST_SHP)

        with fiona.open(DST_SHP) as dst:
            for record in dst:
                self.assertEqual(
                    record.get('geometry').get('type'), EXPECTED_TYPE)

    def test__shp_to_shp_record_count_is_3(self):
        EXPECTED_COUNT = 3

        DST_SHP = os.path.join(TMP_DIR, 'centerlines.shp')
        create_centerlines(src=self.INPUT_SHP, dst=DST_SHP)

        with fiona.open(DST_SHP) as dst:
            self.assertEqual(len(list(dst)), EXPECTED_COUNT)

    def test__shp_to_geojson_execution_successful_returns_None(self):
        DST_GEOJSON = os.path.join(TMP_DIR, 'centerlines.geojson')

        output = create_centerlines(src=self.INPUT_SHP, dst=DST_GEOJSON)
        self.assertIsNone(output)

    def test__shp_to_geojson_records_geom_type_is_multilinestring(self):
        EXPECTED_TYPE = 'MultiLineString'

        DST_GEOJSON = os.path.join(TMP_DIR, 'centerlines.geojson')
        create_centerlines(src=self.INPUT_SHP, dst=DST_GEOJSON)

        with fiona.open(DST_GEOJSON) as dst:
            for record in dst:
                self.assertEqual(
                    record.get('geometry').get('type'), EXPECTED_TYPE)

    def test__shp_to_geojson_record_count_is_3(self):
        EXPECTED_COUNT = 3

        DST_GEOJSON = os.path.join(TMP_DIR, 'centerlines.geojson')
        create_centerlines(src=self.INPUT_SHP, dst=DST_GEOJSON)

        with fiona.open(DST_GEOJSON) as dst:
            self.assertEqual(len(list(dst)), EXPECTED_COUNT)

    def test_invalid_destination_file_format(self):
        DST_SHP = os.path.join(TMP_DIR, 'centerlines.something')
        with self.assertRaises(ValueError):
            create_centerlines(src=self.INPUT_SHP, dst=DST_SHP)

    def test__input_file_does_not_contain_polygons(self):
        EXPECTED_COUNT = 0

        INPUT_FILE = os.path.join(GEOJSON_DIR, 'points.geojson')
        DST_GEOJSON = os.path.join(TMP_DIR, 'centerlines.geojson')

        create_centerlines(src=INPUT_FILE, dst=DST_GEOJSON)

        with fiona.open(DST_GEOJSON) as dst:
            self.assertEqual(len(list(dst)), EXPECTED_COUNT)
