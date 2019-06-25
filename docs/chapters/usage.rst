Usage
*****

Command-line interface
======================

This library provides the ``create_centerlines`` command-line script for creating centerlines from a vector source file and saving them into a destination vector file. The script supports all OGR's vector file formats which enables conversion between different formats:

.. code:: bash

    $ create_centerlines input.shp output.geojson


Python
======

If you want to create your own scripts or use the ``Centerline`` class directly, you can import it:

.. code:: python

    from centerline.geometry import Centerline
