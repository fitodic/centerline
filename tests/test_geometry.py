# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest

from shapely import geometry

from centerline.exceptions import InvalidInputTypeError, TooFewRidgesError
from centerline.geometry import Centerline


def test_creating_centerline_from_polygon_returns_centerline(simple_polygon):
    centerline = Centerline(simple_polygon)
    assert isinstance(centerline, Centerline)
    assert isinstance(centerline.geometry, geometry.MultiLineString)


def test_creating_centerline_from_complex_polygon_returns_centerline(
    complex_polygon,
):
    centerline = Centerline(complex_polygon)

    assert isinstance(centerline, Centerline)
    assert isinstance(centerline.geometry, geometry.MultiLineString)


def test_creating_centerline_from_multipolygon_returns_centerline(
    multipolygon,
):
    centerline = Centerline(multipolygon)
    assert isinstance(centerline, Centerline)
    assert isinstance(centerline.geometry, geometry.MultiLineString)


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
    multilinestring,
):
    with pytest.raises(InvalidInputTypeError):
        Centerline(multilinestring)


def test_creating_centerline_from_geometry_collection_raises_typeerror(
    geometry_collection,
):
    with pytest.raises(InvalidInputTypeError):
        Centerline(geometry_collection)


def test_creating_centerline_using_too_large_interp_dist_raises_runtimeerror(
    create_polygon,
):
    polygon = create_polygon(exterior=[[0, 0], [10, 0], [10, 10], [0, 10]])
    with pytest.raises(TooFewRidgesError):
        Centerline(polygon, 10)

    centerline = Centerline(polygon, 5)
    assert isinstance(centerline, Centerline)
    assert isinstance(centerline.geometry, geometry.MultiLineString)


def test_centerline_has_attributes_assigned_to_it(simple_polygon):
    ATTRIBUTES = {"id": 1, "name": "polygon", "valid": True}

    centerline = Centerline(simple_polygon, **ATTRIBUTES)

    assert isinstance(centerline, Centerline)
    assert isinstance(centerline.geometry, geometry.MultiLineString)
    assert centerline.id == ATTRIBUTES.get("id")
    assert centerline.name == ATTRIBUTES.get("name")
    assert centerline.valid == ATTRIBUTES.get("valid")


def test_centerline_has_length_greater_than_zero(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.geometry.length > 0


def test_centerline_geometry_is_valid(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.geometry.is_valid is True


def test_centerline_is_not_empty(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.geometry.is_empty is False


def test_centerline_is_simple(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.geometry.is_simple is True


def test_centerline_does_not_touch_the_polygons_boundary(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert centerline.geometry.intersects(complex_polygon.boundary) is False


def test_polygon_contains_the_centerline(complex_polygon):
    centerline = Centerline(complex_polygon)
    assert complex_polygon.contains(centerline.geometry) is True


def test_qhull_error(create_polygon):
    # https://github.com/fitodic/centerline/issues/24
    polygon = create_polygon(
        exterior=[
            (107, 189),
            (106, 190),
            (100, 190),
            (99, 191),
            (95, 191),
            (94, 192),
            (92, 192),
            (91, 193),
            (90, 193),
            (89, 194),
            (88, 194),
            (87, 195),
            (86, 195),
            (85, 196),
            (84, 196),
            (82, 198),
            (82, 203),
            (86, 207),
            (87, 207),
            (90, 210),
            (91, 210),
            (92, 211),
            (94, 211),
            (95, 212),
            (98, 212),
            (99, 213),
            (101, 213),
            (102, 214),
            (105, 214),
            (106, 215),
            (108, 215),
            (109, 216),
            (111, 216),
            (112, 217),
            (114, 217),
            (115, 218),
            (117, 218),
            (118, 219),
            (120, 219),
            (121, 220),
            (126, 220),
            (127, 221),
            (133, 221),
            (134, 222),
            (136, 222),
            (137, 223),
            (138, 223),
            (139, 224),
            (139, 227),
            (137, 229),
            (137, 230),
            (136, 231),
            (135, 231),
            (133, 233),
            (132, 233),
            (130, 235),
            (129, 235),
            (126, 238),
            (125, 238),
            (124, 239),
            (123, 239),
            (122, 240),
            (121, 240),
            (120, 241),
            (119, 241),
            (118, 242),
            (116, 242),
            (115, 243),
            (114, 243),
            (113, 244),
            (112, 244),
            (110, 246),
            (109, 246),
            (108, 247),
            (107, 247),
            (106, 248),
            (105, 248),
            (104, 249),
            (102, 249),
            (101, 250),
            (99, 250),
            (98, 251),
            (97, 251),
            (96, 252),
            (94, 252),
            (92, 254),
            (91, 254),
            (90, 255),
            (89, 255),
            (88, 256),
            (87, 256),
            (86, 257),
            (85, 257),
            (84, 258),
            (83, 258),
            (82, 259),
            (80, 259),
            (79, 260),
            (78, 260),
            (70, 268),
            (70, 269),
            (69, 270),
            (69, 272),
            (68, 273),
            (68, 276),
            (71, 279),
            (73, 279),
            (74, 280),
            (83, 280),
            (84, 279),
            (90, 279),
            (91, 278),
            (94, 278),
            (95, 277),
            (97, 277),
            (98, 276),
            (99, 276),
            (100, 275),
            (101, 275),
            (103, 273),
            (105, 273),
            (106, 272),
            (108, 272),
            (109, 271),
            (111, 271),
            (112, 270),
            (113, 270),
            (114, 269),
            (115, 269),
            (116, 268),
            (117, 268),
            (120, 265),
            (121, 265),
            (122, 264),
            (124, 264),
            (125, 263),
            (126, 263),
            (127, 262),
            (128, 262),
            (129, 261),
            (130, 261),
            (132, 259),
            (133, 259),
            (135, 257),
            (136, 257),
            (137, 256),
            (138, 256),
            (139, 255),
            (141, 255),
            (142, 254),
            (143, 254),
            (145, 252),
            (146, 252),
            (149, 249),
            (150, 249),
            (153, 246),
            (154, 246),
            (158, 242),
            (158, 241),
            (164, 235),
            (164, 234),
            (165, 233),
            (165, 232),
            (166, 231),
            (166, 230),
            (167, 229),
            (167, 227),
            (168, 226),
            (168, 223),
            (169, 222),
            (169, 220),
            (170, 219),
            (170, 212),
            (169, 211),
            (169, 210),
            (168, 209),
            (168, 208),
            (167, 207),
            (167, 206),
            (162, 201),
            (161, 201),
            (159, 199),
            (158, 199),
            (157, 198),
            (155, 198),
            (154, 197),
            (153, 197),
            (151, 195),
            (150, 195),
            (149, 194),
            (147, 194),
            (146, 193),
            (144, 193),
            (143, 192),
            (139, 192),
            (138, 191),
            (132, 191),
            (131, 190),
            (122, 190),
            (121, 189),
        ]
    )
    attributes = {"id": 1, "name": "polygon", "valid": True}
    centerline = Centerline(polygon, **attributes)

    assert isinstance(centerline, Centerline)
    assert isinstance(centerline.geometry, geometry.MultiLineString)
