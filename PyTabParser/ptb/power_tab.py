import os.path

from PyTabParser import ByteReader, TabException

FILE_TYPE_SONG = 0
FILE_TYPE_LESSON = 1

FILE_CONTENTS_BASS = True
FILE_CONTENTS_GUITAR = False

FILE_VERSION_UNKNOWN = 0
FILE_VERSION_1_0 = 1
FILE_VERSION_1_0_2 = 2
FILE_VERSION_1_5 = 3
FILE_VERSION_1_7 = 4

class PowerTab:
  VERSION = "ptab-4"

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
        self.initialize()
    except TabException as error:
      raise error
    except:
      raise Exception(f"Corrupt file [{self.file_path}]")  

  def initialize(self):
    self._read_version()
    self._initialize_metadata()

  def get_version(self):
    return self.version

  def get_metadata(self):
    return self.metadata

  def _read_version(self):
    version = self.byte_reader.readStringBytes(4)
    num = self.byte_reader.readShort()
    self.version = f"{version}-{num}"
    if not num in [1, 2, 3, 4]:
      raise TabException(f"Invalid PowerTab file version=[{self.version}] [{self.file_path}]")

  def _initialize_metadata(self): 
    file_version = int(self.get_version().split('-')[1])
    if file_version == FILE_VERSION_1_7:
      file_type = self.byte_reader.readByteAsInt()
      self.metadata['file_type'] = file_type
      if file_type == FILE_TYPE_SONG:
        self.byte_reader.skip(1) # File content (bass or guitar)
        self.metadata['title'] = self.byte_reader.readString() 
        self.metadata['artist'] = self.byte_reader.readString() 
      else:
        self.metadata['title'] = self.byte_reader.readString() 
        self.metadata['artist'] = self.byte_reader.readString() 

