# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from unittest import TestCase

from centerline.main import Centerline as BaseCenterline


class TestInit(TestCase):

    def test_centerline_import__import_successful(self):
        """An ImportError should not be raised."""
        from centerline import Centerline
        self.assertEqual(Centerline, BaseCenterline)
