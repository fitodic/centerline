# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from unittest import TestCase


class TestInit(TestCase):

    def test_centerline_import__import_successful(self):
        """ImportError should not be raised!"""
        from centerline import Centerline
