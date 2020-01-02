.. centerline documentation master file, created by
   sphinx-quickstart on Sun Jun 23 15:35:54 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to centerline's documentation!
======================================

.. image:: https://travis-ci.org/fitodic/centerline.svg?branch=master
    :target: https://travis-ci.org/fitodic/centerline
    :alt: Build

.. image:: https://readthedocs.org/projects/centerline/badge/?version=latest
    :target: http://centerline.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/fitodic/centerline/badge.svg?branch=master
    :target: https://coveralls.io/github/fitodic/centerline?branch=master
    :alt: Coverage

.. image:: https://img.shields.io/pypi/v/centerline.svg
    :target: https://pypi.python.org/pypi/centerline
    :alt: Version

.. image:: https://pepy.tech/badge/centerline
    :target: https://pepy.tech/project/centerline
    :alt: Downloads

Roads, rivers and similar linear structures are often represented by long and complex polygons. Since one of the most important attributes of a linear structure is its length, extracting that attribute from a polygon can prove to be more or less difficult.

This library tries to solve this problem by creating the the polygon's centerline using the `Voronoi diagram <https://en.wikipedia.org/wiki/Voronoi_diagram>`_.

.. figure::  images/example.png
   :align:   center

   The source and the output geometry visualized in `QGIS <https://www.qgis.org/en/site/>`_.


Features
^^^^^^^^

* A command-line script for creating centerlines from a vector source file and saving them into a destination vector file: ``create_centerlines``

.. code:: bash

    $ create_centerlines input.shp output.geojson


* The ``Centerline`` class that allows integration into your own workflow.


.. code:: python

    >>> from shapely.geometry import Polygon
    >>> from centerline.geometry import Centerline

    >>> polygon = Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])
    >>> attributes = {"id": 1, "name": "polygon", "valid": True}

    >>> centerline = Centerline(polygon, **attributes)
    >>> centerline.id == 1
    True
    >>> centerline.name
    'polygon'
    >>> centerline.geoms
    <shapely.geometry.base.GeometrySequence object at 0x7f7d24116210>


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   chapters/installation.rst
   chapters/usage.rst
   modules/centerline.rst
   chapters/faq.rst
   chapters/contributing.rst
   chapters/changelog.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
