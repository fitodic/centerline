# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest

from shapely import geometry

from centerline.exceptions import InvalidInputTypeError, TooFewRidgesError
from centerline.geometry import Centerline


def test_creating_centerline_from_polygon_returns_centerline(simple_polygon):
    centerline = Centerline(simple_polygon)
    assert isinstance(centerline, Centerline)
    assert isinstance(centerline, geometry.MultiLineString)


def test_creating_centerline_from_complex_polygon_returns_centerline(
    complex_polygon
):
    centerline = Centerline(complex_polygon)

    assert isinstance(centerline, Centerline)
    assert isinstance(centerline, geometry.MultiLineString)


def test_creating_centerline_from_multipolygon_returns_centerline(
    multipolygon
):
    centerline = Centerline(multipolygon)
    assert isinstance(centerline, Centerline)
    assert isinstance(centerline, geometry.MultiLineString)


def test_creating_centerline_from_point_raises_typeerror(point):
    with pytest.raises(InvalidInputTypeError):
        Centerline(point)


def test_creating_centerline_from_multipoint_raises_typeerror(multipoint):
    with pytest.raises(InvalidInputTypeError):
        Centerline(multipoint)


def test_creating_centerline_from_linestring_raises_typeerror(linestring):
    with pytest.raises(InvalidInputTypeError):
        Centerline(linestring)


def test_creating_centerline_from_multilinestring_raises_typeerror(
    multilinestring
):
    with pytest.raises(InvalidInputTypeError):
        Centerline(multilinestring)


def test_creating_centerline_from_geometry_collection_raises_typeerror(
    geometry_collection
):
    with pytest.raises(InvalidInputTypeError):
        Centerline(geometry_collection)


def test_creating_centerline_using_too_large_interp_dist_raises_runtimeerror(
    create_polygon
):
    polygon = create_polygon(exterior=[[0, 0], [10, 0], [10, 10], [0, 10]])
    with pytest.raises(TooFewRidgesError):
        Centerline(polygon, 10)

    centerline = Centerline(polygon, 5)
    assert isinstance(centerline, Centerline)
    assert isinstance(centerline, geometry.MultiLineString)


def test_centerline_has_attributes_assigned_to_it(simple_polygon):
    ATTRIBUTES = {"id": 1, "name": "polygon", "valid": True}

    centerline = Centerline(simple_polygon, **ATTRIBUTES)

    assert isinstance(centerline, Centerline)
    assert isinstance(centerline, geometry.MultiLineString)
    assert centerline.id == ATTRIBUTES.get("id")
    assert centerline.name == ATTRIBUTES.get("name")
    assert centerline.valid == ATTRIBUTES.get("valid")


def test_centerline_has_length_greater_than_zero(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.length > 0


def test_centerline_geometry_is_valid(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.is_valid is True


def test_centerline_is_not_empty(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.is_empty is False


def test_centerline_is_simple(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.is_simple is True


def test_centerline_does_not_touch_the_polygons_boundary(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.intersects(complex_polygon.boundary) is False


def test_polygon_contains_the_centerline(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert complex_polygon.contains(centerline) is True
