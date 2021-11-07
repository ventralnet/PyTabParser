import os
import unittest

from PyTabParser import Guitarpro6Tab

class GuitarPro6TabTest(unittest.TestCase):

  def setUp(self):
    self.resource_folder = f"{os.path.dirname(__file__)}/../resources/guitarpro"

  def assert_metadata_field(self, field_name, expected):
    self.assertEqual(self.tab.get_metadata()[field_name], expected)

  def test_get_version(self):
    self.tab = Guitarpro6Tab(os.path.abspath(f"{self.resource_folder}/gpx2.gpx"))
 
