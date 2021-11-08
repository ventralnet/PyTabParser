from PyTabParser import BaseGuitarproTab, TabException

class Guitarpro3Tab(BaseGuitarproTab):
  SUPPORTED_VERSIONS = ["FICHIER GUITAR PRO v3.00"]

  def __init__(self, file_path):
    super(Guitarpro3Tab, self).__init__(file_path)

  def initialize(self):
    self.metadata["title"] = self.readStringByteSizeOfInteger()
    self.readStringByteSizeOfInteger()
    self.metadata["artist"] = self.readStringByteSizeOfInteger()
    self.metadata["album"] = self.readStringByteSizeOfInteger()
    self.metadata["author"] = self.readStringByteSizeOfInteger()
    self.metadata["copyright"] = self.readStringByteSizeOfInteger()
    self.metadata["writer"] = self.readStringByteSizeOfInteger()