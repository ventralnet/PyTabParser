import os
import unittest

from PyTabParser import PowerTab

class PowerTabTest:
  def setUp(self):
    self.resource_folder = f"{os.path.dirname(__file__)}/../resource/ptb"

  def test_get_version():
    self.power_tab = PowerTab(os.path.abspath("f{self.resource_folder}/test-song-public-release.ptb"))
    assert_equal(self.power_tab.getVersion(), "ptb-4")

if __name__ == '__main__':
  unittest.main()
