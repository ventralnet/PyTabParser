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

  def initialize(self):
    self.metadata["title"] = self.readStringByteSizeOfInteger()
    self.readStringByteSizeOfInteger()
    self.metadata["artist"] = self.readStringByteSizeOfInteger()
    self.metadata["album"] = self.readStringByteSizeOfInteger()
    self.metadata["author"] = self.readStringByteSizeOfInteger()
    self.metadata["copyright"] = self.readStringByteSizeOfInteger()
    self.metadata["writer"] = self.readStringByteSizeOfInteger()

  def __initialize(self):
    self._read_version()
    self.initialize()

  def _read_version(self):
    try:
      length = self.byte_reader.readByteAsInt()
      stringLength = length if length >= 0 and length <= 30 else 30
      self.version = self.byte_reader.readStringBytes(stringLength)
      pad_length = 30 - length
      self.byte_reader.skip(pad_length)
      self.version = self.version[0:stringLength]
    except(UnicodeDecodeError):
      self.version = 'CANT READ VERSION'
      
  def get_metadata(self):
    return self.metadata

#    version = self.byte_reader.readStringLength(4)
#    num = self.byte_reader.readShort()
#    self.version = f"{version}-{num}"
#    if not num in [1, 2, 3, 4]:
#      raise TabException(f"Invalid PowerTab file version=[{self.version}] [{self.file_path}]")

  def get_version(self):
    return self.version

  def readStringByteSizeOfInteger(self):
    return self.readStringByte( self.byte_reader.readInt() - 1 )

  def readStringByte(self, size):
    return self.readString(size, self.byte_reader.readByteAsInt())

  def readString(self, size, len):
    string_len = len if len >= 0 and len <= size else size
    pad_bytes = len - string_len
    result = self.byte_reader.readStringBytes(string_len)
    self.byte_reader.skip(pad_bytes)
    return result
