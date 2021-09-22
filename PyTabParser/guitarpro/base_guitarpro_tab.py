import os

from PyTabParser import ByteReader, TabException

from abc import ABC, abstractmethod

class BaseGuitarproTab(ABC):
  def __init__(self, file_path):
    if not os.path.exists(file_path):
      raise Exception(f'[{file_path}] does not exist')

    if not os.path.isfile(file_path):
      raise Exception(f'[{file_path}] is not a file')

    try:
      self.file_path = file_path
      with open(file_path, 'rb') as file:
        self.byte_reader = ByteReader(file)
        self.metadata = dict()
        self.__initialize()
    except TabException as error:
      raise error
    except:
      raise Exception(f"Corrupt file [{self.file_path}]")  

  @abstractmethod
  def initialize(self):
    pass

  def __initialize(self):
    self._read_version()
    self.initialize()

  def _read_version(self):
    try:
      self.version = self.byte_reader.readString(30)
      print(f"{self.version}   {self.file_path}")
    except(UnicodeDecodeError):
      self.version = 'CANT READ VERSION'
      
#    version = self.byte_reader.readStringLength(4)
#    num = self.byte_reader.readShort()
#    self.version = f"{version}-{num}"
#    if not num in [1, 2, 3, 4]:
#      raise TabException(f"Invalid PowerTab file version=[{self.version}] [{self.file_path}]")

  def get_version(self):
    return self.version
