#polygon-centerline
------------------
##Calculates the centerline of a polygon.

Roads, rivers and similar linear structures are often represented by long and complex polygons. Since one of the most important attributes of a linear structure is its length, extracting that attribute from a polygon can prove to be more or less difficult.

There are two Python scripts. The first one, *centerline.py* handles the basic computations and can be used as a stand-alone script. The second one, *shp2centerline.py* has a more specific nature. The input is a Shapefile that contains polygons. It takes each polygon and calculates its centerline by calling the *centerline.py*. The output is also a Shapefile which contains MultiLineStrings.

------------------

###Usage:
In order to calculate the centerlines from the polygons saved within a Shapefile, open the Terminal (Ctrl + Alt + T) and type:
```
$ python shp2centerline.py INPUT_SHP OUTPUT_SHP BORDER_DENSITY
```
The BORDER_DENSITY parameter is optional. If not specified, the default value is 0.5. For more information type:
```
$ python shp2centerline.py -h
```
**Warning**:
The INPUT_SHP file needs to have a column called **id** with unique values or the script will fail to execute successfully.

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
When defining the density factor, one has to take into account the coordinate system defined in the Shapefile. The script was designed to handle metric coordinate systems, so the density factor is by default 0.5 (meters). For instance, if the value is set to 0.5 m, it basically places additional points on the border at the distance of 0.5 m from each other. If the user doesn't define the value (see *Usage*), the script uses the default value. If the value is a negative number, it will be converted into a positive number. 

It appears that the Voronoi function available in the *SciPy* module does not handle large coordinates very well. Since most of the coordinates are large numbers, a bounding box is needed to determine the minimal X and Y coordinates, i.e. the bottom left corner of the bounding box. These values are then used for coordinate reduction. Once the Voronoi diagram is created the coordinates are returned to their non-reduced form before creating linestrings.

**Example**
![Screenshot](Screenshot.png)