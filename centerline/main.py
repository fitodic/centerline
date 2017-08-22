# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from numpy import array
from scipy.spatial import Voronoi
from shapely.geometry import LineString, MultiLineString, MultiPolygon, Polygon
from shapely.ops import unary_union


class Centerline(MultiLineString):

    def __init__(self, input_geom, interpolation_distance=0.5):
        """Create a centerline object.

        Args:
            input_geom {Polygon} or {MultiPolygon}: shapely geometry
            interpolation_distance {float}: interpolation distance [m]

        Returns:
            {MultiPolygon}: centerline geometry

        Raises:
            {ValueError}: invalid input geometry

        Extends:
            {MultiLineString}

        """

        if not (isinstance(input_geom, Polygon) or
                isinstance(input_geom, MultiPolygon)):
            raise ValueError(
                'Input geometry must be either a shapely.geometry.Polygon '
                'or a shapely.geometry.MultiPolygon instance'
            )

        self._input_geom = input_geom
        self._interpolation_distance = abs(interpolation_distance)
        # Values used for temporary coordinate reduction
        self._minx = int(min(self._input_geom.envelope.exterior.xy[0]))
        self._miny = int(min(self._input_geom.envelope.exterior.xy[1]))

        super(Centerline, self).__init__(lines=self._create_centerline())

    def _create_centerline(self):
        """
        Calculates the centerline of a polygon.

        Densifies the border of a polygon which is then represented by a Numpy
        array of points necessary for creating the Voronoi diagram. Once the
        diagram is created, the ridges located within the polygon are
        joined and returned.

        Returns:
            a union of lines that are located within the polygon.
        """

        border = array(self.__densify_border())

        vor = Voronoi(border)
        vertex = vor.vertices

        lst_lines = []
        for j, ridge in enumerate(vor.ridge_vertices):
            if -1 not in ridge:
                line = LineString([
                    (vertex[ridge[0]][0] + self._minx,
                     vertex[ridge[0]][1] + self._miny),
                    (vertex[ridge[1]][0] + self._minx,
                     vertex[ridge[1]][1] + self._miny)])

                if line.within(self._input_geom) and len(line.coords[0]) > 1:
                    lst_lines.append(line)

        return unary_union(lst_lines)

    def __densify_border(self):
        """Densify the border of a polygon.

        The border is densified  by a given factor (by default: 0.5).

        The complexity of the polygon's geometry is evaluated in order
        to densify the borders of its interior rings as well.

        Returns:
            {list}: a list of points where each point is represented by
                a list of its reduced coordinates
                (e.g. [[X1, Y1], [X2, Y2], ..., [Xn, Yn])

        """

        if len(self._input_geom.interiors) == 0:
            exterIN = LineString(self._input_geom.exterior)
            points = self.__fixed_interpolation(exterIN)

        else:
            exterIN = LineString(self._input_geom.exterior)
            points = self.__fixed_interpolation(exterIN)

            for j in range(len(self._input_geom.interiors)):
                interIN = LineString(self._input_geom.interiors[j])
                points += self.__fixed_interpolation(interIN)

        return points

    def __fixed_interpolation(self, line):
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

        count = self._interpolation_distance

        STARTPOINT = [line.xy[0][0] - self._minx, line.xy[1][0] - self._miny]
        ENDPOINT = [line.xy[0][-1] - self._minx, line.xy[1][-1] - self._miny]

        newline = []
        newline.append(STARTPOINT)

        while count < line.length:
            point = line.interpolate(count)
            newline.append([point.x - self._minx, point.y - self._miny])
            count += self._interpolation_distance

        newline.append(ENDPOINT)

        return newline