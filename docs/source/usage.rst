Usage
*****

Command-line interface
======================

This library provides a command-line tool for creating centerlines from a vector source file and saving them into a destination vector file: `create_centerlines`.

.. code:: bash

    $ create_centerlines -h
    usage: create_centerlines [-h] SRC DEST [BORDENS]

    Calculate the centerline of a polygon

    positional arguments:
      SRC         Name of the input Shapefile
      DEST        Name of the output Shapefile
      BORDENS     The density of the border. Defaults to 0.5 (meters)

    optional arguments:
      -h, --help  show this help message and exit


The `create_centerlines` script is file format agnostic, meaning you should be able to work with all OGR's vector file formats:

.. code:: bash

    $ create_centerlines input.shp output.geojson


Python
======

If you need to customize the creation of centerlines in any way, simply import the `Centerline` class and use it or extend it::

    from centerline.main import Centerline
