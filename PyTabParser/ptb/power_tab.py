import os.path

from PyByteReader import ByteReader

class PowerTab:
  def __init__(self, file_path):
    if not os.path.exists(file_path):
      raise Exception(f'[{file_path}] does not exist')

    if not os.path.isfile(file_path):
      raise Exception(f'[{file_path}] is not a file')

    with open(file_path, 'rb') as file:
      self.byte_reader = ByteReader(file)
      self.song_info = { }
      self.initialize()

  def initialize(self):
    self._read_version()
    #    self._read_song_info()

  def get_version(self):
    return self.version

  def get_song_info(self):
    #    return self.song_info
    pass

  def _read_version(self):
    version = self.byte_reader.readStringLength(4)
    num = str(self.byte_reader.readShort())
    self.version = f"{version}-{num}"
    print(self.version)

#  def _read_song_info(self):
#    self.classification = self.byte_reader.readBoolean()
#    if self.classification == False:
#      # Classification is Song
#      self.byte_reader.skip(1)
#      self.song_info['name'] = self.byte_reader.readString()
#      self.song_info['artist'] = self.byte_reader.readString()
#      
#      release_type = self.byte_reader.readByteAsInt()
#      self.song_info['release_type'] = release_type
#      if release_type == 0:
#        self.song_info['album_type'] = self.byte_reader.readByteAsInt()
#        self.song_info['album'] = self.byte_reader.readString()
#        self.song_info['year'] = self.byte_reader.readShort()
#        self.song_info['is_live_recording'] = self.byte_reader.readBoolean()
#      elif release_type == 1:
#        self.song_info['album'] = self.byte_reader.readString()
#        self.song_info['is_live_recording'] = self.byte_reader.readBoolean()
#      elif release_type == 2:
#        self.song_info['album'] = self.byte_reader.readString()
#        self.song_info['day'] = self.byte_reader.readShort()
#        self.song_info['month'] = self.byte_reader.readShort()
#        self.song_info['year'] = self.byte_reader.readShort()
#        if self.byte_reader.readByte() == 0:
#          self.song_info['author'] = self.byte_reader.readString()
#          self.song_info['lyricist'] = self.byte_reader.readString()
#        self.song_info['music_by'] = self.byte_reader.readString()
#        self.song_info['guitar_transcriber'] = self.byte_reader.readString()
#        self.song_info['bass_transcriber'] = self.byte_reader.readString()
#        self.song_info['copyright'] = self.byte_reader.readString()
#        self.song_info['lyrics'] = self.byte_reader.readString()
#        self.song_info['guitar_instructions'] = self.byte_reader.readString()
#        self.song_info['bass_instructions'] = self.byte_reader.readString()
#    elif self.classification == True:
#      # Classification is Lesson
#      self.song_info['name'] = self.byte_reader.readString()
#      self.song_info['album'] = self.byte_reader.readString()
#      self.song_info['style'] = self.byte_reader.readShort()
#      self.song_info['level'] = self.byte_reader.readByteAsInt()
#      self.song_info['author'] = self.byte_reader.readString()
#      self.song_info['instructions'] = self.byte_reader.readString()
#      self.song_info['copyright'] = self.byte_reader.readString()

