# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from numpy import array
from scipy.spatial import Voronoi
from shapely.geometry import LineString
from shapely.ops import unary_union


class Centerline(object):

    def __init__(self, input_geom, dist=0.5):
        self.input_geom = input_geom
        self.dist = abs(dist)

        self.minx = int(min(self.input_geom.envelope.exterior.xy[0]))
        self.miny = int(min(self.input_geom.envelope.exterior.xy[1]))

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

        border = array(self.densify_border())

        vor = Voronoi(border)
        vertex = vor.vertices

        lst_lines = []
        for j, ridge in enumerate(vor.ridge_vertices):
            if -1 not in ridge:
                line = LineString([
                    (vertex[ridge[0]][0] + self.minx,
                     vertex[ridge[0]][1] + self.miny),
                    (vertex[ridge[1]][0] + self.minx,
                     vertex[ridge[1]][1] + self.miny)])

                if line.within(self.input_geom) and len(line.coords[0]) > 1:
                    lst_lines.append(line)

        return unary_union(lst_lines)

    def densify_border(self):
        """Densify the border of a polygon.

        The border is densified  by a given factor (by default: 0.5).

        The complexity of the polygon's geometry is evaluated in order
        to densify the borders of its interior rings as well.

        Returns:
            {list}: a list of points where each point is represented by
                a list of its reduced coordinates
                (e.g. [[X1, Y1], [X2, Y2], ..., [Xn, Yn])

        """

        if len(self.input_geom.interiors) == 0:
            exterIN = LineString(self.input_geom.exterior)
            points = self.fixed_interpolation(exterIN)

        else:
            exterIN = LineString(self.input_geom.exterior)
            points = self.fixed_interpolation(exterIN)

            for j in range(len(self.input_geom.interiors)):
                interIN = LineString(self.input_geom.interiors[j])
                points += self.fixed_interpolation(interIN)

        return points

    def fixed_interpolation(self, line):
        """Place additional points on the border at the specified distance.

        By default the distance is 0.5 (meters) which means that the first
        point will be placed 0.5 m from the starting point, the second
        point will be placed at the distance of 1.0 m from the first
        point, etc. The loop breaks when the summarized distance exceeds
        the length of the line.

        Args:
            line {shapely.geometry.LineString}: object

        Returns:
            {list}: a list of points where each point is represented by
                a list of its reduced coordinates
                (e.g. [[X1, Y1], [X2, Y2], ..., [Xn, Yn])

        """

        count = self.dist

        STARTPOINT = [line.xy[0][0] - self.minx, line.xy[1][0] - self.miny]
        ENDPOINT = [line.xy[0][-1] - self.minx, line.xy[1][-1] - self.miny]

        newline = []
        newline.append(STARTPOINT)

        while count < line.length:
            point = line.interpolate(count)
            newline.append([point.x - self.minx, point.y - self.miny])
            count += self.dist

        newline.append(ENDPOINT)

        return newline
