from PyTabParser import BaseGuitarproTab, TabException

class Guitarpro3Tab(BaseGuitarproTab):
  def __init__(self, file_path):
    super(Guitarpro3Tab, self).__init__(file_path)

  def _read_version(self):
    length = self.byte_reader.readByteAsInt()
    stringLength = length if length >= 0 and length <= 30 else 30
    self.version = self.byte_reader.readStringBytes(stringLength)

  def initialize(self):
    pass
