# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class CenterlineError(Exception):
    default_message = "An error has occured while constucting the centerline."

    def __init__(self, *args, **kwargs):  # pragma: no cover
        if not (args or kwargs):
            args = (self.default_message,)

        super(CenterlineError, self).__init__(*args, **kwargs)


class InvalidInputTypeError(CenterlineError):
    default_message = (
        "Input geometry must be of type shapely.geometry.Polygon "
        "or shapely.geometry.MultiPolygon!"
    )


class TooFewRidgesError(CenterlineError):
    default_message = (
        "Number of produced ridges is too small. Please adjust your "
        "interpolation distance."
    )


class UnsupportedVectorType(CenterlineError):
    default_message = "No OGR driver was found for the provided file."
