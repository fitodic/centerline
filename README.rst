Centerline
==========

.. image:: https://github.com/fitodic/centerline/actions/workflows/ci.yml/badge.svg?event=push
    :target: https://github.com/fitodic/centerline/actions
    :alt: Build status

.. image:: https://codecov.io/gh/fitodic/centerline/branch/master/graph/badge.svg?token=S2WQ9OTR9O
    :target: https://codecov.io/gh/fitodic/centerline
    :alt: Test coverage status

.. image:: https://readthedocs.org/projects/centerline/badge/?version=latest
    :target: http://centerline.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/centerline.svg
    :target: https://pypi.python.org/pypi/centerline
    :alt: Version

.. image:: https://pepy.tech/badge/centerline
    :target: https://pepy.tech/project/centerline
    :alt: Downloads

.. figure::  docs/images/example.png
   :align:   center

Roads, rivers and similar linear structures are often represented by
long and complex polygons. Since one of the most important attributes of
a linear structure is its length, extracting that attribute from a
polygon can prove to be more or less difficult.

This library tries to solve this problem by creating the the polygon's
centerline using the `Voronoi diagram
<https://en.wikipedia.org/wiki/Voronoi_diagram>`_. For more info on how
to use this package, see the
`official documentation <http://centerline.readthedocs.io/>`_.


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
    >>> centerline.geometry.geoms
    <shapely.geometry.base.GeometrySequence object at 0x7f7d24116210>
