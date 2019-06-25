# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import shutil

import pytest

from shapely import geometry


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_DIR = os.path.join(TESTS_DIR, "tmp")
TEST_DATA_DIR = os.path.join(TESTS_DIR, "data")
SHP_DIR = os.path.join(TEST_DATA_DIR, "shp")
GEOJSON_DIR = os.path.join(TEST_DATA_DIR, "geojson")


@pytest.fixture
def point():
    return geometry.Point(0, 0)


@pytest.fixture
def multipoint():
    return geometry.MultiPoint([geometry.Point(0, 0), geometry.Point(1, 1)])


@pytest.fixture
def linestring():
    return geometry.LineString([(0, 0), (0.8, 0.8), (1.8, 0.95), (2.6, 0.5)])


@pytest.fixture
def multilinestring():
    return geometry.MultiLineString([((0, 0), (1, 1)), ((-1, 0), (1, 0))])


@pytest.fixture
def multipolygon():
    polygon_1 = geometry.Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])
    polygon_2 = geometry.Polygon([[5, 5], [5, 9], [9, 9], [9, 5]])

    return geometry.MultiPolygon([polygon_1, polygon_2])


@pytest.fixture
def geometry_collection():
    return geometry.GeometryCollection(
        (
            geometry.Point(0, 0),
            geometry.LineString([(0, 0), (0.8, 0.8), (1.8, 0.95), (2.6, 0.5)]),
            geometry.Polygon([[0, 0], [0, 4], [4, 4], [4, 0]]),
        )
    )


@pytest.fixture
def simple_polygon(create_polygon):
    return create_polygon(exterior=[[0, 0], [0, 4], [4, 4], [4, 0]])


@pytest.fixture
def complex_polygon(create_polygon):
    exterior = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
    interior = [(1, 0), (0.5, 0.5), (1, 1), (1.5, 0.5), (1, 0)][::-1]
    return create_polygon(exterior, [interior])


@pytest.fixture
def create_polygon():
    def _create_polygon(exterior, holes=None):
        return geometry.Polygon(exterior, holes)

    return _create_polygon


@pytest.fixture
def create_input_file():
    def _create_input_file(filename, extension):
        extension_directories = {"shp": SHP_DIR, "geojson": GEOJSON_DIR}
        directory = extension_directories.get(extension.lower(), TEST_DATA_DIR)
        return os.path.join(
            directory,
            "{filename}.{extension}".format(
                filename=filename, extension=extension
            ),
        )

    os.mkdir(TMP_DIR)
    yield _create_input_file
    shutil.rmtree(TMP_DIR)


@pytest.fixture
def create_output_centerline_file():
    def _create_output_centerline_file(extension):
        return os.path.join(TMP_DIR, "centerlines.{}".format(extension))

    return _create_output_centerline_file
