#polygon-centerline
------------------
##Calculates the centerline of a polygon.

Roads, rivers and similar linear structures are often represented by long and complex polygons. Since one of the most important attributes of a linear structure is its length, extracting that attribute from a polygon can prove to be more or less difficult.

This Python script takes the polygons from a Shapefile, calculates the centerline of each polygon and exports the into a separate Shapefile.

------------------

###Usage:
In order to calculate the centerlines from the polygons saved within a Shapefile, open the Terminal and type:
```
$ python centerline.py INPUT_SHP OUTPUT_SHP INTERPOLATION_DISTANCE
```
The INTERPOLATION_DISTANCE parameter is optional. If not specified, the default value is 0.5. For more information type:
```
$ python centerline.py -h
```

###Requirements:
1. [Python 2.7+](https://www.python.org/download/releases/2.7/)
2. [Shapely](https://pypi.python.org/pypi/Shapely)
3. [SciPy](http://www.scipy.org/)
4. [Fiona](https://pypi.python.org/pypi/Fiona/)
5. [Numpy](http://www.scipy.org/)
6. [ArgParse](https://docs.python.org/2.7/library/argparse.html)

###References:
* [SciPy-Voronoi](http://docs.scipy.org/doc/scipy/reference/tutorial/spatial.html#voronoi-diagrams)

------------------

**Notes**:
When defining the density factor, one has to take into account the coordinate system defined in the Shapefile. The script was designed to handle metric coordinate systems, so the density factor is by default 0.5 (meters). If the user doesn't define the value (see *Usage*), the script uses the default value. If the value is a negative number, it will be converted into a positive number.

It appears that the Voronoi function available in the *SciPy* module does not handle large coordinates very well. Since most of the coordinates are large numbers, a bounding box is needed to determine the minimal X and Y coordinates, i.e. the bottom left corner of the bounding box. These values are then used for coordinate reduction. Once the Voronoi diagram is created the coordinates are returned to their non-reduced form before creating linestrings.

**Example**
![Screenshot](Screenshot.png)