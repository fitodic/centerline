# -*- encoding: utf-8 -*-
from shapely.geometry import LineString, Polygon, MultiLineString, mapping, shape
from shapely.ops import unary_union
from scipy.spatial import Voronoi
import numpy as np
import fiona


class Centerline(object):

	def __init__(self, inputSHP, dist = 0.5):
		self.shp = inputSHP
		self.dist = dist

		print 'Importing Shapefile.'
		self.dct_polygons = self.importSHP()

		print 'Calculating centerlines.'
		self.dct_centerlines = self.createCenterline()

		print 'Exporting ceterlines to Shapefile.'
		self.export2SHP()


	def createCenterline(self):
		"""
		Calculates the centerline of a polygon.

		Densifies the border of a polygon which is then represented by a Numpy
		array of points necessary for creating the Voronoi diagram. Once the 
		diagram is created, the ridges located within the polygon are
		joined and returned.

		Returns:
			a union of lines that are located within the polygon.
		"""
		dct_clines = {}
		for i, key in enumerate(self.dct_polygons.keys()):
			polygon = self.dct_polygons[key][0]
			minx = self.dct_polygons[key][1]
			miny = self.dct_polygons[key][2]

			border = np.array(self.densifyBorder(polygon, minx, miny))

			vor = Voronoi(border)
			vertex = vor.vertices

			lst_lines = []
			for j, ridge in enumerate(vor.ridge_vertices):
				if -1 not in ridge:
					line = LineString([\
						(vertex[ridge[0]][0] + minx, vertex[ridge[0]][1] + miny), \
						(vertex[ridge[1]][0] + minx, vertex[ridge[1]][1] + miny)])

					if line.within(polygon):
						lst_lines.append(line)

			dct_clines[key] = unary_union(lst_lines)

		return dct_clines


	def importSHP(self):
		""" 
		Imports the Shapefile into a dictionary.
		
		Returns:
			a dictionary where the ID is the key, and the value is a list
			that contains the geometry, minimal X and minimal Y coordinate.
		"""

		dct = {}

		with fiona.open(self.shp, 'r', encoding = 'UTF-8') as fileIN:
			for polygon in fileIN:
				polygonID = polygon['properties'][u'id']
				geom = shape(polygon['geometry'])
				minx = int(min(geom.envelope.exterior.xy[0]))
				miny = int(min(geom.envelope.exterior.xy[1]))

				dct[polygonID] = [geom, minx, miny]

		return dct


	def densifyBorder(self, polygon, minx, miny):
		"""
		Densifies the border of a polygon by a given factor (by default: 0.5).

		The function tests the complexity of the polygons geometry, i.e. does 
		the polygon have holes or not. If the polygon doesn't have any holes, 
		its exterior is extracted and densified by a given factor. If the 
		polygon has holes, the boundary of each hole as well as its exterior is 
		extracted and densified by a given factor.

		Returns:
			a list of points where each point is represented by a list of its 
			reduced coordinates.

		Example:
			[[X1, Y1], [X2, Y2], ..., [Xn, Yn]
		"""

		if len(polygon.interiors) == 0:
			exterIN = LineString(polygon.exterior)
			points = self.fixedInterpolation(exterIN, minx, miny)
		
		else:
			exterIN = LineString(polygon.exterior)
			points = self.fixedInterpolation(exterIN, minx, miny)

			for j in range(len(polygon.interiors)):
				interIN = LineString(polygon.interiors[j])
				points += self.fixedInterpolation(interIN, minx, miny)

		return points


	def fixedInterpolation(self, line, minx, miny):
		"""
		A helping function which is used in densifying the border of a polygon.

		It places points on the border at the specified distance. By default the
		distance is 0.5 (meters) which means that the first point will be placed
		0.5 m from the starting point, the second point will be placed at the 
		distance of 1.0 m from the first point, etc. Naturally, the loop breaks 
		when the summarized distance exceeds the length of the line.

		Returns:
			a list of points where each point is represented by a list of its 
			reduced coordinates.

		Example:
			[[X1, Y1], [X2, Y2], ..., [Xn, Yn]
		"""

		count = self.dist
		newline = []

		startpoint = [line.xy[0][0] - minx, line.xy[1][0] - miny]
		endpoint = [line.xy[0][-1] - minx, line.xy[1][-1] - miny]
		newline.append(startpoint)

		while count < line.length:
			point = line.interpolate(count)
			newline.append([point.x - minx, point.y - miny])
			count += self.dist

		newline.append(endpoint)

		return newline


	def export2SHP(self):
		"""
		Creates a Shapefile and fills it centerlines and their IDs.

		The dictionary contains the IDs of the centerlines (keys) and their 
		geometries (values). The ID of a centerline is the same as the ID of 
		the polygon it represents.
		"""

		newschema = {'geometry': 'MultiLineString', 'properties': {'id': 'int'}}

		with fiona.open('centerlines.shp', 'w', encoding='UTF-8', \
			schema = newschema, driver = 'ESRI Shapefile') as SHPfile:
			
			for i, key in enumerate(self.dct_centerlines):
				geom = self.dct_centerlines[key]
				newline = {}

				newline['geometry'] = mapping(geom)
				newline['properties'] = {'id': key}

				SHPfile.write(newline)


if __name__ == "__main__":
	Centerline('inputSHP.shp', 0.5)