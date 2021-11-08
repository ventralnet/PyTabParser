class ByteReader:
  def __init__(self, file_input):
    self.file_input = file_input

  def skip(self, bytes = 1):
    self.file_input.read(bytes)

  def readStringBytes(self, bytes, encoding = 'utf-8'):
    return self.file_input.read(bytes).decode('utf-8')

  def readString(self, encoding = 'utf-8'):
    defined_length = self.readByteAsInt()
    string = self.readStringBytes(defined_length) 
    return string

  def readInt(self):
    bytes = self.file_input.read(4)
    return ((bytes[3] & 0xff) << 24) | ((bytes[2] & 0xff) << 16) | ((bytes[1] & 0xff) << 8) | (bytes[0] & 0xff)

  def readShort(self):
    bytes = self.file_input.read(2)
    return ((bytes[1] & 0xff) << 8) | (bytes[0] & 0xff)

  def readByteAsInt(self):
    return int.from_bytes(self.file_input.read(1), 'big')
