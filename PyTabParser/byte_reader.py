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

  def readByteAsInt(self):
    return int.from_bytes(self.file_input.read(1), 'big')
