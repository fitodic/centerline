# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## 0.2.2 - Unreleased

### Added

- `flake8` configuration
- `flake8` checks in the Travis build

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
