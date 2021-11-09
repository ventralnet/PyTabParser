from PyTabParser import BaseGuitarproTab, TabException

class GuitarproTab(BaseGuitarproTab):
  SUPPORTED_VERSIONS = ["FICHIER GUITAR PRO v3.00"]

  def __init__(self, file_path):
    super(GuitarproTab, self).__init__(file_path)

