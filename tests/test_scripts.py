# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import shutil

import fiona
import pytest

from centerline.exceptions import InvalidInputTypeError
from centerline.converters import get_ogr_driver


def test__driver_name__with_shp__returns_esri_shapefile(create_input_file):
    EXPECTED_DRIVER_NAME = "ESRI Shapefile"

    input_file = create_input_file("polygons", "shp")
    driver = get_ogr_driver(input_file)

    assert driver.GetName() == EXPECTED_DRIVER_NAME


def test__driver_name__with_json__returns_geojson(create_input_file):
    EXPECTED_DRIVER_NAME = "GeoJSON"
    input_file = "example.json"

    driver = get_ogr_driver(input_file)

    assert driver.GetName() == EXPECTED_DRIVER_NAME


def test__driver_name__with_geojson__returns_geojson(create_input_file):
    EXPECTED_DRIVER_NAME = "GeoJSON"
    input_file = create_input_file("polygons", "geojson")

    driver = get_ogr_driver(input_file)

    assert driver.GetName() == EXPECTED_DRIVER_NAME


def test__with_unknown_extension__returns_valueerror():
    input_file = "example.unknown"

    with pytest.raises(InvalidInputTypeError):
        get_ogr_driver(input_file)


@pytest.mark.script_launch_mode("subprocess")
def test_shp_to_shp_too_large_density_raises_error(
    create_input_file, create_output_centerline_file, caplog, script_runner
):
    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_shp = create_output_centerline_file("shp")
    output = script_runner.run(
        "create_centerlines.py",
        input_polygon_shp,
        output_centerline_shp,
        "13.5",
    )

    assert (
        "Number of produced ridges is too small. Please adjust your "
        "interpolation distance." in output.stderr
    )


def test_shp_to_shp_records_geom_type_is_multilinestring(
    create_input_file, create_output_centerline_file, script_runner
):
    EXPECTED_TYPE = "MultiLineString"

    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_shp = create_output_centerline_file("shp")
    script_runner.run(
        "create_centerlines.py", input_polygon_shp, output_centerline_shp
    )

    with fiona.open(output_centerline_shp) as dst:
        for record in dst:
            assert record.get("geometry").get("type") == EXPECTED_TYPE


def test_shp_to_shp_record_count_is_3(
    create_input_file, create_output_centerline_file, script_runner
):
    EXPECTED_COUNT = 3

    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_shp = create_output_centerline_file("shp")
    script_runner.run(
        "create_centerlines.py", input_polygon_shp, output_centerline_shp
    )

    with fiona.open(output_centerline_shp) as dst:
        assert len(list(dst)) == EXPECTED_COUNT


def test_shp_to_geojson_records_geom_type_is_multilinestring(
    create_input_file, create_output_centerline_file, script_runner
):
    EXPECTED_TYPE = "MultiLineString"

    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_geojson = create_output_centerline_file("geojson")
    script_runner.run(
        "create_centerlines.py", input_polygon_shp, output_centerline_geojson
    )

    with fiona.open(output_centerline_geojson) as dst:
        for record in dst:
            assert record.get("geometry").get("type") == EXPECTED_TYPE


def test_shp_to_geojson_record_count_is_3(
    create_input_file, create_output_centerline_file, script_runner
):
    EXPECTED_COUNT = 3

    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_geojson = create_output_centerline_file("geojson")
    script_runner.run(
        "create_centerlines.py", input_polygon_shp, output_centerline_geojson
    )

    with fiona.open(output_centerline_geojson) as dst:
        assert len(list(dst)) == EXPECTED_COUNT


def test_invalid_destination_file_format(
    create_input_file, create_output_centerline_file, script_runner
):
    input_polygon_shp = create_input_file("polygons", "shp")
    output_centerline_file = create_output_centerline_file("unknown")

    output = script_runner.run(
        "create_centerlines.py", input_polygon_shp, output_centerline_file
    )
    assert (
        "No driver found for the following file extension: unknown"
        in output.stderr
    )


def test_input_file_does_not_contain_polygons(
    create_input_file, create_output_centerline_file, script_runner
):
    EXPECTED_COUNT = 0

    input_points_geojson = create_input_file("points", "geojson")
    output_centerline_geojson = create_output_centerline_file("geojson")

    script_runner.run(
        "create_centerlines.py",
        input_points_geojson,
        output_centerline_geojson,
    )

    with fiona.open(output_centerline_geojson) as dst:
        assert len(list(dst)) == EXPECTED_COUNT
