Usage
*****

Command-line interface
======================

This library provides the ``create_centerlines`` command-line script for creating centerlines from a vector source file and saving them into a destination vector file. The script supports all OGR's vector file formats which enables conversion between different formats:

.. code:: bash

    $ create_centerlines input.shp output.geojson


Python
======

If you want to use the ``Centerline`` class directly, you can import it and instatiate it with geometric data (of type ``shapely.geometry.Polygon`` or ``shapely.geometry.MultiPolygon``) and the object's attributes (optional):

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
