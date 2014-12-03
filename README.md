#polygon-centerline
==================

##Calculates the centerline of a polygon.

Roads, rivers and similar linear structures are often represented by long and complex polygons. Since one of the most important attributes of a linear structure is its length, extracting that attribute from a polygon can prove to be more or less difficult.

This Python script takes the polygons from a Shapefile, calculates the centerline of each polygon and exports the into a separate Shapefile.

###Usage:
Before running the script open it and change the name of the input Shapefile (at the bottom of the script). After that, open the Terminal and type:
'''
$ python centerline.py
'''

###Requirements:
1. [Python 2.7+](https://www.python.org/download/releases/2.7/)
2. [Shapely](https://pypi.python.org/pypi/Shapely)
3. [SciPy](http://www.scipy.org/)
4. [Fiona](https://pypi.python.org/pypi/Fiona/)
5. [Numpy](http://www.scipy.org/)

###References:
* [SciPy-Voronoi](http://docs.scipy.org/doc/scipy/reference/tutorial/spatial.html#voronoi-diagrams)

**Notes**:
When defining the density factor, one has to take into account the coordinate system defined in the Shapefile. The script was designed to handle metric coordinate systems, so the density factor is by default 0.5 (meters).

It appears that the Voronoi function available in the *SciPy* module does not handle large coordinates very well. Since most of the coordinates are large numbers, a bounding box is needed to calculate the minimal X and Y coordinates (bottom left corner). These values are then used for coordinate reduction. Once the Voronoi diagram is created the coordinates are returned to their non-reduced form before creating linestrings.

**Example**
![Screenshot](Screenshot.png)
