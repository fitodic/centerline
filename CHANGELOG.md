# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## Unreleased

### Added

- `CHANGELOG.md`
- `.coveragerc`
- Test and package configuration in `setup.cfg`
- Use `pytest` for test execution
- Test the import of the `Centerline` class

### Changed

- `MANIFEST.in`
- `.gitignore`
- Reorganize the project's requirements (both in `*.txt` files and `setup.py`)
- Fix PEP8 errors in `setup.py`

## 0.1 - 2016-01-15

### Added

- The `Centerline` class
- The logic for calculating the centerline of a polygon
- The `shp2centerline` command for converting polygons from a Shapefile
into centerlines and saving them into another Shapefile
