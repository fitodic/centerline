# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## 0.5.2 - 2019-01-27

### Fixed

- Package versioning that caused a broken upload

## 0.5.1 - 2019-01-27

### Changed

- Set the minimum `GDAL` version to 2.3.3

### Fixed

- Drop the `path` keyword argument from `fiona.open` calls [#20](https://github.com/fitodic/centerline/issues/20).

### Removed

- Python 3.5 support


## 0.5 - 2018-09-09

### Added

- `MultiPolygon` support

## 0.4.2 - 2018-08-22

### Added

- `GDAL` 2.3.1 to the CI configuration

### Changed

- Moved the `coverage` configuration to `setup.cfg`
- Moved the package's metadata to `setup.cfg`

### Fixed

- Error when `MultiLineString` degenerates into `LineString` ([#14](https://github.com/fitodic/centerline/issues/14)). Thanks [mxwell](https://github.com/mxwell)!

### Removed

- MANIFEST.in
- `Centerline` from the `centerline` namespace. To import the `Centerline`
    class, use `from centerline.main import Centerline`

## 0.4.1 - 2018-01-07

### Fixed

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
