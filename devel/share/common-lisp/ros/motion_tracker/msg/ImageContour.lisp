; Auto-generated. Do not edit!


(cl:in-package motion_tracker-msg)


;//! \htmlinclude ImageContour.msg.html

(cl:defclass <ImageContour> (roslisp-msg-protocol:ros-message)
  ((ann_file
    :reader ann_file
    :initarg :ann_file
    :type cl:string
    :initform "")
   (frame
    :reader frame
    :initarg :frame
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image))
   (prevFrame
    :reader prevFrame
    :initarg :prevFrame
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image))
   (gray_frame
    :reader gray_frame
    :initarg :gray_frame
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass ImageContour (<ImageContour>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImageContour>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImageContour)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name motion_tracker-msg:<ImageContour> is deprecated: use motion_tracker-msg:ImageContour instead.")))

(cl:ensure-generic-function 'ann_file-val :lambda-list '(m))
(cl:defmethod ann_file-val ((m <ImageContour>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motion_tracker-msg:ann_file-val is deprecated.  Use motion_tracker-msg:ann_file instead.")
  (ann_file m))

(cl:ensure-generic-function 'frame-val :lambda-list '(m))
(cl:defmethod frame-val ((m <ImageContour>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motion_tracker-msg:frame-val is deprecated.  Use motion_tracker-msg:frame instead.")
  (frame m))

(cl:ensure-generic-function 'prevFrame-val :lambda-list '(m))
(cl:defmethod prevFrame-val ((m <ImageContour>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motion_tracker-msg:prevFrame-val is deprecated.  Use motion_tracker-msg:prevFrame instead.")
  (prevFrame m))

(cl:ensure-generic-function 'gray_frame-val :lambda-list '(m))
(cl:defmethod gray_frame-val ((m <ImageContour>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motion_tracker-msg:gray_frame-val is deprecated.  Use motion_tracker-msg:gray_frame instead.")
  (gray_frame m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImageContour>) ostream)
  "Serializes a message object of type '<ImageContour>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'ann_file))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'ann_file))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'frame) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'prevFrame) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'gray_frame) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImageContour>) istream)
  "Deserializes a message object of type '<ImageContour>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ann_file) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'ann_file) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'frame) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'prevFrame) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'gray_frame) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImageContour>)))
  "Returns string type for a message object of type '<ImageContour>"
  "motion_tracker/ImageContour")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImageContour)))
  "Returns string type for a message object of type 'ImageContour"
  "motion_tracker/ImageContour")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImageContour>)))
  "Returns md5sum for a message object of type '<ImageContour>"
  "ec56e43facaaa5042c6f1314b2415932")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImageContour)))
  "Returns md5sum for a message object of type 'ImageContour"
  "ec56e43facaaa5042c6f1314b2415932")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImageContour>)))
  "Returns full string definition for message of type '<ImageContour>"
  (cl:format cl:nil "string ann_file~%sensor_msgs/Image frame~%sensor_msgs/Image prevFrame~%sensor_msgs/Image gray_frame~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImageContour)))
  "Returns full string definition for message of type 'ImageContour"
  (cl:format cl:nil "string ann_file~%sensor_msgs/Image frame~%sensor_msgs/Image prevFrame~%sensor_msgs/Image gray_frame~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImageContour>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'ann_file))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'frame))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'prevFrame))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'gray_frame))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImageContour>))
  "Converts a ROS message object to a list"
  (cl:list 'ImageContour
    (cl:cons ':ann_file (ann_file msg))
    (cl:cons ':frame (frame msg))
    (cl:cons ':prevFrame (prevFrame msg))
    (cl:cons ':gray_frame (gray_frame msg))
))
