# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## 0.4.1 - 2018-01-07

## Fixed

- Ignore the `osgeo` package when building the documentation on [readthedocs.org](https://readthedocs.org/)

## 0.4 - 2018-01-07

### Added

- Sphinx documentation

### Fixed

- Add a comma to the list of development requirements


## 0.3 - 2017-11-26

### Added

- `pylama` and `isort` configuration
- `pylama` and `isort` checks in the Travis build
- `utils` and `io` modules
- `create_centerlines` script and function for creating centerlines that is format agnotic. All OGR vector file formats should be supported.

### Changed

- The `Centerline` class extends Shapely's `MultiLineString` class
- Replaced the `shp2centerline` script with `create_centerlines`

### Removed

- Support for `GDAL<2.0`
- Support for `Fiona<1.7`
- `shp2centerline` script


## 0.2.1 - 2017-06-18

### Fixed

- Read the `README.rst` from `setup.py`

## 0.2 - 2017-06-18

### Added

- `CHANGELOG.md`
- `.coveragerc`
- Travis CI configuration
- Test and package configuration in `setup.cfg`
- Use `pytest` for test execution
- Test the import of the `Centerline` class

### Changed

- `MANIFEST.in`
- `.gitignore`
- Reorganize the project's requirements (both in `*.txt` files and `setup.py`)
- Fix PEP8 errors in `setup.py`
- Convert README from MarkDown to ReStructuredText

## 0.1 - 2016-01-15

### Added

- The `Centerline` class
- The logic for calculating the centerline of a polygon
- The `shp2centerline` command for converting polygons from a Shapefile
into centerlines and saving them into another Shapefile
