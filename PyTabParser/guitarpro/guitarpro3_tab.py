from PyTabParser import BaseGuitarproTab, TabException

class Guitarpro3Tab(BaseGuitarproTab):
  SUPPORTED_VERSIONS = ["FICHIER GUITAR PRO v3.00"]

  def __init__(self, file_path):
    super(Guitarpro3Tab, self).__init__(file_path)

  def initialize(self):
    metadata = self.metadata
    len = self.byte_reader.readInt()
    metadata["title"] = len