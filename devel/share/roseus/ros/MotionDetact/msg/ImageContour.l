;; Auto-generated. Do not edit!


(when (boundp 'MotionDetact::ImageContour)
  (if (not (find-package "MOTIONDETACT"))
    (make-package "MOTIONDETACT"))
  (shadow 'ImageContour (find-package "MOTIONDETACT")))
(unless (find-package "MOTIONDETACT::IMAGECONTOUR")
  (make-package "MOTIONDETACT::IMAGECONTOUR"))

(in-package "ROS")
;;//! \htmlinclude ImageContour.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass MotionDetact::ImageContour
  :super ros::object
  :slots (_frame _firstFrame _gray_frame ))

(defmethod MotionDetact::ImageContour
  (:init
   (&key
    ((:frame __frame) (instance sensor_msgs::Image :init))
    ((:firstFrame __firstFrame) (instance sensor_msgs::Image :init))
    ((:gray_frame __gray_frame) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _frame __frame)
   (setq _firstFrame __firstFrame)
   (setq _gray_frame __gray_frame)
   self)
  (:frame
   (&rest __frame)
   (if (keywordp (car __frame))
       (send* _frame __frame)
     (progn
       (if __frame (setq _frame (car __frame)))
       _frame)))
  (:firstFrame
   (&rest __firstFrame)
   (if (keywordp (car __firstFrame))
       (send* _firstFrame __firstFrame)
     (progn
       (if __firstFrame (setq _firstFrame (car __firstFrame)))
       _firstFrame)))
  (:gray_frame
   (&rest __gray_frame)
   (if (keywordp (car __gray_frame))
       (send* _gray_frame __gray_frame)
     (progn
       (if __gray_frame (setq _gray_frame (car __gray_frame)))
       _gray_frame)))
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/Image _frame
    (send _frame :serialization-length)
    ;; sensor_msgs/Image _firstFrame
    (send _firstFrame :serialization-length)
    ;; sensor_msgs/Image _gray_frame
    (send _gray_frame :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/Image _frame
       (send _frame :serialize s)
     ;; sensor_msgs/Image _firstFrame
       (send _firstFrame :serialize s)
     ;; sensor_msgs/Image _gray_frame
       (send _gray_frame :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/Image _frame
     (send _frame :deserialize buf ptr-) (incf ptr- (send _frame :serialization-length))
   ;; sensor_msgs/Image _firstFrame
     (send _firstFrame :deserialize buf ptr-) (incf ptr- (send _firstFrame :serialization-length))
   ;; sensor_msgs/Image _gray_frame
     (send _gray_frame :deserialize buf ptr-) (incf ptr- (send _gray_frame :serialization-length))
   ;;
   self)
  )

(setf (get MotionDetact::ImageContour :md5sum-) "99ce6b969f78ad0c2518c2eacf95bee1")
(setf (get MotionDetact::ImageContour :datatype-) "MotionDetact/ImageContour")
(setf (get MotionDetact::ImageContour :definition-)
      "sensor_msgs/Image frame
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

")



(provide :MotionDetact/ImageContour "99ce6b969f78ad0c2518c2eacf95bee1")


