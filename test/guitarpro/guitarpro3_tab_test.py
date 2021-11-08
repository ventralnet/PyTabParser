import os
import unittest

from PyTabParser import Guitarpro3Tab

class GuitarPro3TabTest(unittest.TestCase):

  def setUp(self):
    self.resource_folder = f"{os.path.dirname(__file__)}/../resources/gp/"
    self.tab = Guitarpro3Tab(os.path.abspath(f"{self.resource_folder}/gp3.gp3"))

  def assert_metadata_field(self, field_name, expected):
    self.assertEqual(self.tab.get_metadata()[field_name], expected)

  # def test_get_version(self):
  #   self.assertEqual(self.tab.version, "FICHIER GUITAR PRO v3.00")

  def test_attributes(self):
    self.assert_metadata_field('title', "Stages") 
    self.assert_metadata_field('artist', "ZZ Top") 
    self.assert_metadata_field('album', "Afterburner") 
    self.assert_metadata_field('author', "test author") 
    self.assert_metadata_field('copyright', "test copyright") 
    self.assert_metadata_field('writer', "test tab creator") 

if __name__ == '__main__':
  unittest.main()