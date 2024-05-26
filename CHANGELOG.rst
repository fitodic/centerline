*********
Changelog
*********

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_ and this project adheres to `Semantic Versioning <http://semver.org/>`_.

Changes for the upcoming release can be found in the `changelog.d` directory in this repository. Do **NOT** add changelog entries here! This changelog is managed by `towncrier <https://github.com/hawkowl/towncrier>`_ and is compiled at release time.

.. towncrier release notes start

1.1.1 (2024-05-26)
-------------------

Bugfixes
^^^^^^^^

- Adding `predicate` as a named parameter in `str_tree.query` (`#47 <https://github.com/fitodic/centerline/pull/47>`_)


1.1.0 (2024-02-10)
-------------------

Features
^^^^^^^^

- Convert the centerline within check to use Shapely STRTrees (`#44 <https://github.com/fitodic/centerline/pull/44>`_)


1.0.1 (2023-01-23)
-------------------

Misc
^^^^

- Restore Python 3.7+ support and update metadata. (`#39 <https://github.com/fitodic/centerline/pull/39>`_)


1.0.0 (2023-01-07)
-------------------

Features
^^^^^^^^

- Add support for Shapely 2 (`#30 <https://github.com/fitodic/centerline/pull/30>`_)


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

- * The `Centerline` class will no longer extend the Shapely's `MultiLineString` because `Centerline` sets custom attributes which will be prohibited starting from Shapely 2.0. You can use `centerline.geometry` instead of `centerline` wherever you need access to the object's geometry.
  * Drop Python 2.7 support (`#30 <https://github.com/fitodic/centerline/pull/30>`_)


0.6.4 (2022-09-17)
-------------------

Bugfixes
^^^^^^^^

- Fix shapely 2 deprecation warning for iterating multipolygons (`#34 <https://github.com/fitodic/centerline/pull/34>`_)


0.6.3 (2020-01-02)
-------------------

No significant changes.


0.6.2 (2020-01-02)
-------------------

Misc
^^^^

- Update the CI deploy stage. (`#26 <https://github.com/fitodic/centerline/pull/26>`_)


0.6.1 (2020-01-02)
-------------------

Misc
^^^^

- Run the test suite against Python 3.8. (`#25 <https://github.com/fitodic/centerline/pull/25>`_)


0.6.0 (2019-06-25)
-------------------

Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

- Replace `argparse <https://docs.python.org/3/library/argparse.html>`_ with `Click <https://click.palletsprojects.com/en/7.x/>`_. This should improve Windows support of the ``create_centerline`` command-line script. (`#23 <https://github.com/fitodic/centerline/pull/23>`_)


Misc
^^^^

- Convert the package to the `src/ layout <https://setuptools.readthedocs.io/en/latest/setuptools.html#using-a-src-layout>`_ and the tests to `pytest <https://docs.pytest.org/en/latest/>`_. The modules have been renamed, and the ``Centerline`` class has been refactored to enable overrides. (`#23 <https://github.com/fitodic/centerline/pull/23>`_)


0.5.2 (2019-01-27)
------------------

Fixed
^^^^^

- Package versioning that caused a broken upload

0.5.1 (2019-01-27)
------------------

Changed
^^^^^^^

- Set the minimum ``GDAL`` version to 2.3.3

Fixed
^^^^^

- Drop the ``path`` keyword argument from ``fiona.open`` calls `#20 <https://github.com/fitodic/centerline/issues/20>`_.

Removed
^^^^^^^

- Python 3.5 support


0.5.0 (2018-09-09)
----------------

Added
^^^^^

- ``MultiPolygon`` support

0.4.2 (2018-08-22)
------------------

Added
^^^^^

- ``GDAL`` 2.3.1 to the CI configuration


Changed
^^^^^^^

- Moved the ``coverage`` configuration to ``setup.cfg``
- Moved the package's metadata to ``setup.cfg``


Fixed
^^^^^

- Error when ``MultiLineString`` degenerates into ``LineString`` (`#14 <https://github.com/fitodic/centerline/issues/14>`_). Thanks `mxwell <https://github.com/mxwell>`_!


Removed
^^^^^^^

- MANIFEST.in
- ``Centerline`` from the ``centerline`` namespace. To import the ``Centerline``
    class, use ``from centerline.main import Centerline``

0.4.1 (2018-01-07)
------------------

Fixed
^^^^^

- Ignore the ``osgeo`` package when building the documentation on `readthedocs.org <https://readthedocs.org/>`_.

0.4.0 (2018-01-07)
----------------

Added
^^^^^

- Sphinx documentation


Fixed
^^^^^

- Add a comma to the list of development requirements


0.3.0 (2017-11-26)
----------------

Added
^^^^^

- ``pylama`` and ``isort`` configuration
- ``pylama`` and ``isort`` checks in the Travis build
- ``utils`` and ``io`` modules
- ``create_centerlines`` script and function for creating centerlines that is format agnotic. All OGR vector file formats should be supported.


Changed
^^^^^^^

- The ``Centerline`` class extends Shapely's ``MultiLineString`` class
- Replaced the ``shp2centerline`` script with ``create_centerlines``


Removed
^^^^^^^

- Support for ``GDAL<2.0``
- Support for ``Fiona<1.7``
- ``shp2centerline`` script


0.2.1 (2017-06-18)
------------------

Fixed
^^^^^

- Read the ``README.rst`` from ``setup.py``

0.2.0 (2017-06-18)
----------------

Added
^^^^^

- ``CHANGELOG.md``
- ``.coveragerc``
- Travis CI configuration
- Test and package configuration in ``setup.cfg``
- Use ``pytest`` for test execution
- Test the import of the ``Centerline`` class


Changed
^^^^^^^

- ``MANIFEST.in``
- ``.gitignore``
- Reorganize the project's requirements (both in ``*.txt`` files and ``setup.py``)
- Fix PEP8 errors in ``setup.py``
- Convert README from MarkDown to ReStructuredText

0.1.0 (2016-01-15)
----------------

Added
^^^^^

- The ``Centerline`` class
- The logic for calculating the centerline of a polygon
- The ``shp2centerline`` command for converting polygons from a Shapefile into centerlines and saving them into another Shapefile
