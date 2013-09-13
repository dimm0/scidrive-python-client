import os

class AnalyzeFileObjBug(Exception):
    msg = ("\n"
           "Expected file object to have %d bytes, instead we read %d bytes.\n"
           "File size detection may have failed (see dropbox.util.AnalyzeFileObj)\n")
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

    def __str__(self):
        return self.msg % (self.expected, self.actual)

def analyze_file_obj(obj):
    """ Get the size and contents of a file-like object.
        Returns:  (size, raw_data)
                  size: The amount of data waiting to be read
                  raw_data: If not None, the entire contents of the stream (as a string).
                            None if the stream should be read() in chunks.
    """
    pos = 0
    if hasattr(obj, 'tell'):
        pos = obj.tell()

    # Handle real files
    if hasattr(obj, 'fileno'):
        size = max(0, os.fstat(obj.fileno()).st_size - pos)
        return (size, None)

    # User-defined object with len()
    if hasattr(obj, '__len__'):
        size = max(0, len(obj) - pos)
        return (size, None)

    # We don't know what kind of stream this is.
    # To determine the size, we must read the whole thing.
    raw_data = obj.read()
    return (len(raw_data), raw_data)
