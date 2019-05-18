# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest
from shapely import geometry


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
