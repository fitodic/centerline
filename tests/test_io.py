# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import shutil

import fiona
import pytest

from centerline.exceptions import InvalidInputTypeError, TooFewRidgesError
from centerline.io import create_centerlines


def test_shp_to_shp_too_large_density_raises_error(
    create_input_file, create_output_centerline_file, caplog
):
    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_shp = create_output_centerline_file("shp")
    create_centerlines(
        src=input_polygon_shp, dst=output_centerline_shp, density=13.5
    )
    assert TooFewRidgesError.default_message in caplog.messages


def test_shp_to_shp_records_geom_type_is_multilinestring(
    create_input_file, create_output_centerline_file
):
    EXPECTED_TYPE = "MultiLineString"

    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_shp = create_output_centerline_file("shp")
    create_centerlines(src=input_polygon_shp, dst=output_centerline_shp)

    with fiona.open(output_centerline_shp) as dst:
        for record in dst:
            assert record.get("geometry").get("type") == EXPECTED_TYPE


def test_shp_to_shp_record_count_is_3(
    create_input_file, create_output_centerline_file
):
    EXPECTED_COUNT = 3

    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_shp = create_output_centerline_file("shp")
    create_centerlines(src=input_polygon_shp, dst=output_centerline_shp)

    with fiona.open(output_centerline_shp) as dst:
        assert len(list(dst)) == EXPECTED_COUNT


def test_shp_to_geojson_records_geom_type_is_multilinestring(
    create_input_file, create_output_centerline_file
):
    EXPECTED_TYPE = "MultiLineString"

    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_geojson = create_output_centerline_file("geojson")
    create_centerlines(src=input_polygon_shp, dst=output_centerline_geojson)

    with fiona.open(output_centerline_geojson) as dst:
        for record in dst:
            assert record.get("geometry").get("type") == EXPECTED_TYPE


def test_shp_to_geojson_record_count_is_3(
    create_input_file, create_output_centerline_file
):
    EXPECTED_COUNT = 3

    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_geojson = create_output_centerline_file("geojson")
    create_centerlines(src=input_polygon_shp, dst=output_centerline_geojson)

    with fiona.open(output_centerline_geojson) as dst:
        assert len(list(dst)) == EXPECTED_COUNT


def test_invalid_destination_file_format(
    create_input_file, create_output_centerline_file
):
    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_file = create_output_centerline_file("unknown")
    with pytest.raises(InvalidInputTypeError):
        create_centerlines(src=input_polygon_shp, dst=output_centerline_file)


def test_input_file_does_not_contain_polygons(
    create_input_file, create_output_centerline_file
):
    EXPECTED_COUNT = 0

    input_points_geojson = create_input_file("points", "geojson")
    output_centerline_geojson = create_output_centerline_file("geojson")

    create_centerlines(src=input_points_geojson, dst=output_centerline_geojson)

    with fiona.open(output_centerline_geojson) as dst:
        assert len(list(dst)) == EXPECTED_COUNT
