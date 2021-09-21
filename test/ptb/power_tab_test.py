import os
import unittest

from PyTabParser import PowerTab, FILE_TYPE_SONG, FILE_TYPE_LESSON

class PowerTabTest(unittest.TestCase):

  def setUp(self):
    self.resource_folder = f"{os.path.dirname(__file__)}/../resources/ptb"

  def assert_metadata_field(self, field_name, expected):
    self.assertEqual(self.powertab.get_metadata()[field_name], expected)

  def test_get_version(self):
    self.powertab = PowerTab(os.path.abspath(f"{self.resource_folder}/test-song-public-release.ptb"))
    self.assertEqual(self.powertab.get_version(), "ptab-4")

  def test_get_metadata_lesson_type(self):
    self.powertab = PowerTab(os.path.abspath(f"{self.resource_folder}/test-lesson.ptb"))
    self.assert_metadata_field('file_type', FILE_TYPE_LESSON) 
    self.powertab = PowerTab(os.path.abspath(f"{self.resource_folder}/test-song.ptb"))
    self.assert_metadata_field('file_type', FILE_TYPE_SONG) 

  def test_get_title(self):
    self.powertab = PowerTab(os.path.abspath(f"{self.resource_folder}/test-song.ptb"))
    self.assert_metadata_field('title', 'Test Title')
    self.powertab = PowerTab(os.path.abspath(f"{self.resource_folder}/test-lesson.ptb"))
    self.assert_metadata_field('title', 'Test Title') 

  def test_get_song(self):
    self.powertab = PowerTab(os.path.abspath(f"{self.resource_folder}/test-song.ptb"))
    self.assert_metadata_field('artist', 'Test Artist')
    self.powertab = PowerTab(os.path.abspath(f"{self.resource_folder}/test-lesson.ptb"))
    self.assert_metadata_field('artist', 'Test Subtitle') 

if __name__ == '__main__':
  unittest.main()

