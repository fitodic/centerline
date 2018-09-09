# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from unittest import TestCase

from shapely.geometry import (
    GeometryCollection, LineString, MultiLineString, MultiPoint, MultiPolygon,
    Point, Polygon
)

from centerline.main import Centerline


class TestCenterlineSupportedGeometryTypes(TestCase):
    """
    Only Polygons and MultiPolygons should be supported.

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
        POLYGON_1 = Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])
        POLYGON_2 = Polygon([[5, 5], [5, 9], [9, 9], [9, 5]])

        MULTIPOLYGON = MultiPolygon([POLYGON_1, POLYGON_2])

        centerline = Centerline(MULTIPOLYGON)

        self.assertIsInstance(centerline, MultiLineString)

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
        MULTILINESTRING = MultiLineString([((0, 0), (1, 1)), ((-1, 0), (1,
                                                                        0))])

        with self.assertRaises(ValueError):
            Centerline(MULTILINESTRING)

    def test__geometry_collection__raises_valueerror(self):
        GEOMETRY_COLLECTION = GeometryCollection(
            (Point(0, 0),
             LineString([(0, 0), (0.8, 0.8), (1.8, 0.95), (2.6, 0.5)]),
             Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])))

        with self.assertRaises(ValueError):
            Centerline(GEOMETRY_COLLECTION)

    def test__too_large_interp_dist__raises_runtimeerror(self):
        POLYGON = Polygon([[0, 0], [10, 0], [10, 10], [0, 10]])

        with self.assertRaises(RuntimeError):
            Centerline(POLYGON, 10)

        centerline = Centerline(POLYGON, 5)
        self.assertIsInstance(centerline, Centerline)


class TestCenterlineAttributes(TestCase):
    """The attributes should be copied and assigned to the object."""

    def test__object_has_assigned_attributes(self):
        POLYGON = Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])
        ATTRIBUTES = {'id': 1, 'name': 'polygon', 'valid': True}

        centerline = Centerline(POLYGON, **ATTRIBUTES)

        self.assertEqual(centerline.id, ATTRIBUTES.get('id'))
        self.assertEqual(centerline.name, ATTRIBUTES.get('name'))
        self.assertEqual(centerline.valid, ATTRIBUTES.get('valid'))


class TestCenterlineGeometricFeaturesWithASimplePolygon(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.POLYGON = Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])
        cls.CENTERLINE = Centerline(cls.POLYGON)

    def test__is_multilinestring(self):
        self.assertIsInstance(self.CENTERLINE, MultiLineString)

    def test__length__greater_than_zero(self):
        MIN_LENGTH = 0
        self.assertGreater(self.CENTERLINE.length, MIN_LENGTH)

    def test__is_valid(self):
        self.assertTrue(self.CENTERLINE.is_valid)

    def test__is_not_empty(self):
        self.assertFalse(self.CENTERLINE.is_empty)

    def test__is_simple(self):
        self.assertTrue(self.CENTERLINE.is_simple)

    def test__centerline_does_not_touch_the_polygons_boundary(self):
        self.assertFalse(self.CENTERLINE.intersects(self.POLYGON.boundary))

    def test__polygon_contains_the_centerline(self):
        self.assertTrue(self.POLYGON.contains(self.CENTERLINE))


class TestCenterlineGeometricFeaturesWithAComplexPolygon(TestCase):

    @classmethod
    def setUpClass(cls):
        EXTERIOR = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
        INTERIOR = [(1, 0), (0.5, 0.5), (1, 1), (1.5, 0.5), (1, 0)][::-1]
        cls.POLYGON = Polygon(EXTERIOR, [INTERIOR])
        cls.CENTERLINE = Centerline(cls.POLYGON)

    def test__is_multilinestring(self):
        self.assertIsInstance(self.CENTERLINE, MultiLineString)

    def test__length__greater_than_zero(self):
        MIN_LENGTH = 0
        self.assertGreater(self.CENTERLINE.length, MIN_LENGTH)

    def test__is_valid(self):
        self.assertTrue(self.CENTERLINE.is_valid)

    def test__is_not_empty(self):
        self.assertFalse(self.CENTERLINE.is_empty)

    def test__is_simple(self):
        self.assertTrue(self.CENTERLINE.is_simple)

    def test__centerline_does_not_touch_the_polygons_boundary(self):
        self.assertFalse(self.CENTERLINE.intersects(self.POLYGON.boundary))

    def test__polygon_contains_the_centerline(self):
        self.assertTrue(self.POLYGON.contains(self.CENTERLINE))
