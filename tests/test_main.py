# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from unittest import TestCase

from centerline import Centerline
from shapely.geometry import (GeometryCollection, LineString, MultiLineString,
                              MultiPoint, MultiPolygon, Point, Polygon)


class TestCenterlineSupportedGeometryTypes(TestCase):
    """Only Polygons should be supported.

    For more information about creating the geometry objects (like the
    ones used below) see The Shapely User Manual:
    https://shapely.readthedocs.io/en/latest/manual.html

    """

    def test__polygon__returns_multilinestring(self):
        POLYGON = Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])

        centerline = Centerline(POLYGON)

        self.assertIsInstance(centerline, MultiLineString)

    def test__polygon_with_interior_ring__returns_multilinestring(self):
        EXTERIOR = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
        INTERIOR = [(1, 0), (0.5, 0.5), (1, 1), (1.5, 0.5), (1, 0)][::-1]
        POLYGON = Polygon(EXTERIOR, [INTERIOR])

        centerline = Centerline(POLYGON)

        self.assertIsInstance(centerline, MultiLineString)

    def test__multipolygon__raises_valueerror(self):
        POLYGONS = [Point(i, 0).buffer(0.1) for i in range(2)]
        MULTIPOLYGON = MultiPolygon(POLYGONS)

        with self.assertRaises(ValueError):
            Centerline(MULTIPOLYGON)

    def test__point__raises_valueerror(self):
        POINT = Point(0, 0)

        with self.assertRaises(ValueError):
            Centerline(POINT)

    def test__multipoint__raises_valueerror(self):
        MULTIPOINT = MultiPoint([Point(0, 0), Point(1, 1)])

        with self.assertRaises(ValueError):
            Centerline(MULTIPOINT)

    def test__linestring__raises_valueerror(self):
        LINESTRING = LineString([(0, 0), (0.8, 0.8), (1.8, 0.95), (2.6, 0.5)])

        with self.assertRaises(ValueError):
            Centerline(LINESTRING)

    def test__multilinestring__raises_valueerror(self):
        MULTILINESTRING = MultiLineString(
            [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
        )

        with self.assertRaises(ValueError):
            Centerline(MULTILINESTRING)

    def test__geometry_collection__raises_valueerror(self):
        GEOMETRY_COLLECTION = GeometryCollection(
            (
                Point(0, 0),
                LineString([(0, 0), (0.8, 0.8), (1.8, 0.95), (2.6, 0.5)]),
                Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])
            )
        )

        with self.assertRaises(ValueError):
            Centerline(GEOMETRY_COLLECTION)


class TestCenterlineAttributes(TestCase):
    """The attributes should be copied and assigned to the object."""

    def test__object_has_assigned_attributes(self):
        POLYGON = Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])
        ATTRIBUTES = {
            'id': 1,
            'name': 'polygon',
            'valid': True
        }

        centerline = Centerline(POLYGON, **ATTRIBUTES)

        self.assertEqual(centerline.id, ATTRIBUTES.get('id'))
        self.assertEqual(centerline.name, ATTRIBUTES.get('name'))
        self.assertEqual(centerline.valid, ATTRIBUTES.get('valid'))
