# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from motion_tracker/ImageContour.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sensor_msgs.msg
import std_msgs.msg

class ImageContour(genpy.Message):
  _md5sum = "ec56e43facaaa5042c6f1314b2415932"
  _type = "motion_tracker/ImageContour"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string ann_file
sensor_msgs/Image frame
sensor_msgs/Image prevFrame
sensor_msgs/Image gray_frame

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['ann_file','frame','prevFrame','gray_frame']
  _slot_types = ['string','sensor_msgs/Image','sensor_msgs/Image','sensor_msgs/Image']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ann_file,frame,prevFrame,gray_frame

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ImageContour, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ann_file is None:
        self.ann_file = ''
      if self.frame is None:
        self.frame = sensor_msgs.msg.Image()
      if self.prevFrame is None:
        self.prevFrame = sensor_msgs.msg.Image()
      if self.gray_frame is None:
        self.gray_frame = sensor_msgs.msg.Image()
    else:
      self.ann_file = ''
      self.frame = sensor_msgs.msg.Image()
      self.prevFrame = sensor_msgs.msg.Image()
      self.gray_frame = sensor_msgs.msg.Image()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.ann_file
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.frame.header.seq, _x.frame.header.stamp.secs, _x.frame.header.stamp.nsecs))
      _x = self.frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.frame.height, _x.frame.width))
      _x = self.frame.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.frame.is_bigendian, _x.frame.step))
      _x = self.frame.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.prevFrame.header.seq, _x.prevFrame.header.stamp.secs, _x.prevFrame.header.stamp.nsecs))
      _x = self.prevFrame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.prevFrame.height, _x.prevFrame.width))
      _x = self.prevFrame.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.prevFrame.is_bigendian, _x.prevFrame.step))
      _x = self.prevFrame.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.gray_frame.header.seq, _x.gray_frame.header.stamp.secs, _x.gray_frame.header.stamp.nsecs))
      _x = self.gray_frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.gray_frame.height, _x.gray_frame.width))
      _x = self.gray_frame.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.gray_frame.is_bigendian, _x.gray_frame.step))
      _x = self.gray_frame.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.frame is None:
        self.frame = sensor_msgs.msg.Image()
      if self.prevFrame is None:
        self.prevFrame = sensor_msgs.msg.Image()
      if self.gray_frame is None:
        self.gray_frame = sensor_msgs.msg.Image()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ann_file = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.ann_file = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.frame.header.seq, _x.frame.header.stamp.secs, _x.frame.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.frame.height, _x.frame.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.frame.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.frame.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.frame.is_bigendian, _x.frame.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.frame.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.prevFrame.header.seq, _x.prevFrame.header.stamp.secs, _x.prevFrame.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.prevFrame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.prevFrame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.prevFrame.height, _x.prevFrame.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.prevFrame.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.prevFrame.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.prevFrame.is_bigendian, _x.prevFrame.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.prevFrame.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.gray_frame.header.seq, _x.gray_frame.header.stamp.secs, _x.gray_frame.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gray_frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gray_frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.gray_frame.height, _x.gray_frame.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gray_frame.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gray_frame.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.gray_frame.is_bigendian, _x.gray_frame.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.gray_frame.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.ann_file
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.frame.header.seq, _x.frame.header.stamp.secs, _x.frame.header.stamp.nsecs))
      _x = self.frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.frame.height, _x.frame.width))
      _x = self.frame.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.frame.is_bigendian, _x.frame.step))
      _x = self.frame.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.prevFrame.header.seq, _x.prevFrame.header.stamp.secs, _x.prevFrame.header.stamp.nsecs))
      _x = self.prevFrame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.prevFrame.height, _x.prevFrame.width))
      _x = self.prevFrame.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.prevFrame.is_bigendian, _x.prevFrame.step))
      _x = self.prevFrame.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.gray_frame.header.seq, _x.gray_frame.header.stamp.secs, _x.gray_frame.header.stamp.nsecs))
      _x = self.gray_frame.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.gray_frame.height, _x.gray_frame.width))
      _x = self.gray_frame.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.gray_frame.is_bigendian, _x.gray_frame.step))
      _x = self.gray_frame.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.frame is None:
        self.frame = sensor_msgs.msg.Image()
      if self.prevFrame is None:
        self.prevFrame = sensor_msgs.msg.Image()
      if self.gray_frame is None:
        self.gray_frame = sensor_msgs.msg.Image()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ann_file = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.ann_file = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.frame.header.seq, _x.frame.header.stamp.secs, _x.frame.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.frame.height, _x.frame.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.frame.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.frame.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.frame.is_bigendian, _x.frame.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.frame.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.prevFrame.header.seq, _x.prevFrame.header.stamp.secs, _x.prevFrame.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.prevFrame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.prevFrame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.prevFrame.height, _x.prevFrame.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.prevFrame.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.prevFrame.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.prevFrame.is_bigendian, _x.prevFrame.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.prevFrame.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.gray_frame.header.seq, _x.gray_frame.header.stamp.secs, _x.gray_frame.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gray_frame.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gray_frame.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.gray_frame.height, _x.gray_frame.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gray_frame.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gray_frame.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.gray_frame.is_bigendian, _x.gray_frame.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.gray_frame.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
