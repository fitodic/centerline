Frequently Asked Questions
**************************

`QH6214 qhull input error: not enough points to construct initial simplex <https://github.com/fitodic/centerline/issues/9>`_
==============================================================================================================================

This error occurs when there is an inconsistency in units. For example,
the input data is in `EPSG:4326 <https://epsg.io/4326>`_ which uses
degrees, whereas the ``create_centerline`` script's default border
density is in meters.

There are two possible solutions to this problem:

    1. Specify the border density in degrees

        .. code:: bash

            $ create_centerlines input.shp output.geojson 0.00001

    2. Transform the input data into a metric system
    (e.g. `EPSG:3857 <https://epsg.io/3857>`_)


`The level of detail is too high/The geometry is too complex <https://github.com/fitodic/centerline/issues/13>`_
================================================================================================================

Adjust the ``create_centerline``'s border density parameter. The script is
ment to serve a wide range of applications, some of which require a
higher level of detail.

Since the
`Voronoi diagram <https://en.wikipedia.org/wiki/Voronoi_diagram>`_ is
used to calculate the centerline's geometry, that means that depending
on the specified border density occasionaly the centerline will have a
few branches sticking out. The branches can be removed manually using
`QGIS <https://www.qgis.org/en/site/>`_.


`Number of produced ridges is too small <https://github.com/fitodic/centerline/issues/14>`_
===========================================================================================

Depending on the polygon's structure and the border density parameter
set by the user, the
`Voronoi algorithm <https://en.wikipedia.org/wiki/Voronoi_diagram>`_
might not be able to produce enough vertices that lie completely inside
the polygon (i.e. do not intersect the polygon's boundary). In that
case, the output centerline can be reduced to a single line or even a
single point.

When the centerline consists of less than two lines, the ``TooFewRidgesError``
is raised, the ``create_centerline`` script skips the geometry in
question and continues processing the other geometries.
