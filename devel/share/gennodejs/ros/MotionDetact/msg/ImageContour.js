// Auto-generated. Do not edit!

// (in-package MotionDetact.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class ImageContour {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.frame = null;
      this.firstFrame = null;
      this.gray_frame = null;
    }
    else {
      if (initObj.hasOwnProperty('frame')) {
        this.frame = initObj.frame
      }
      else {
        this.frame = new sensor_msgs.msg.Image();
      }
      if (initObj.hasOwnProperty('firstFrame')) {
        this.firstFrame = initObj.firstFrame
      }
      else {
        this.firstFrame = new sensor_msgs.msg.Image();
      }
      if (initObj.hasOwnProperty('gray_frame')) {
        this.gray_frame = initObj.gray_frame
      }
      else {
        this.gray_frame = new sensor_msgs.msg.Image();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ImageContour
    // Serialize message field [frame]
    bufferOffset = sensor_msgs.msg.Image.serialize(obj.frame, buffer, bufferOffset);
    // Serialize message field [firstFrame]
    bufferOffset = sensor_msgs.msg.Image.serialize(obj.firstFrame, buffer, bufferOffset);
    // Serialize message field [gray_frame]
    bufferOffset = sensor_msgs.msg.Image.serialize(obj.gray_frame, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ImageContour
    let len;
    let data = new ImageContour(null);
    // Deserialize message field [frame]
    data.frame = sensor_msgs.msg.Image.deserialize(buffer, bufferOffset);
    // Deserialize message field [firstFrame]
    data.firstFrame = sensor_msgs.msg.Image.deserialize(buffer, bufferOffset);
    // Deserialize message field [gray_frame]
    data.gray_frame = sensor_msgs.msg.Image.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += sensor_msgs.msg.Image.getMessageSize(object.frame);
    length += sensor_msgs.msg.Image.getMessageSize(object.firstFrame);
    length += sensor_msgs.msg.Image.getMessageSize(object.gray_frame);
    return length;
  }

  static datatype() {
    // Returns string type for a message object
    return 'MotionDetact/ImageContour';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '99ce6b969f78ad0c2518c2eacf95bee1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    sensor_msgs/Image frame
    sensor_msgs/Image firstFrame
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ImageContour(null);
    if (msg.frame !== undefined) {
      resolved.frame = sensor_msgs.msg.Image.Resolve(msg.frame)
    }
    else {
      resolved.frame = new sensor_msgs.msg.Image()
    }

    if (msg.firstFrame !== undefined) {
      resolved.firstFrame = sensor_msgs.msg.Image.Resolve(msg.firstFrame)
    }
    else {
      resolved.firstFrame = new sensor_msgs.msg.Image()
    }

    if (msg.gray_frame !== undefined) {
      resolved.gray_frame = sensor_msgs.msg.Image.Resolve(msg.gray_frame)
    }
    else {
      resolved.gray_frame = new sensor_msgs.msg.Image()
    }

    return resolved;
    }
};

module.exports = ImageContour;
