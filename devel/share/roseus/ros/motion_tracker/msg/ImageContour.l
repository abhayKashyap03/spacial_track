;; Auto-generated. Do not edit!


(when (boundp 'motion_tracker::ImageContour)
  (if (not (find-package "MOTION_TRACKER"))
    (make-package "MOTION_TRACKER"))
  (shadow 'ImageContour (find-package "MOTION_TRACKER")))
(unless (find-package "MOTION_TRACKER::IMAGECONTOUR")
  (make-package "MOTION_TRACKER::IMAGECONTOUR"))

(in-package "ROS")
;;//! \htmlinclude ImageContour.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass motion_tracker::ImageContour
  :super ros::object
  :slots (_ann_file _frame _prevFrame _gray_frame ))

(defmethod motion_tracker::ImageContour
  (:init
   (&key
    ((:ann_file __ann_file) "")
    ((:frame __frame) (instance sensor_msgs::Image :init))
    ((:prevFrame __prevFrame) (instance sensor_msgs::Image :init))
    ((:gray_frame __gray_frame) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _ann_file (string __ann_file))
   (setq _frame __frame)
   (setq _prevFrame __prevFrame)
   (setq _gray_frame __gray_frame)
   self)
  (:ann_file
   (&optional __ann_file)
   (if __ann_file (setq _ann_file __ann_file)) _ann_file)
  (:frame
   (&rest __frame)
   (if (keywordp (car __frame))
       (send* _frame __frame)
     (progn
       (if __frame (setq _frame (car __frame)))
       _frame)))
  (:prevFrame
   (&rest __prevFrame)
   (if (keywordp (car __prevFrame))
       (send* _prevFrame __prevFrame)
     (progn
       (if __prevFrame (setq _prevFrame (car __prevFrame)))
       _prevFrame)))
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
    ;; string _ann_file
    4 (length _ann_file)
    ;; sensor_msgs/Image _frame
    (send _frame :serialization-length)
    ;; sensor_msgs/Image _prevFrame
    (send _prevFrame :serialization-length)
    ;; sensor_msgs/Image _gray_frame
    (send _gray_frame :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _ann_file
       (write-long (length _ann_file) s) (princ _ann_file s)
     ;; sensor_msgs/Image _frame
       (send _frame :serialize s)
     ;; sensor_msgs/Image _prevFrame
       (send _prevFrame :serialize s)
     ;; sensor_msgs/Image _gray_frame
       (send _gray_frame :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _ann_file
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _ann_file (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; sensor_msgs/Image _frame
     (send _frame :deserialize buf ptr-) (incf ptr- (send _frame :serialization-length))
   ;; sensor_msgs/Image _prevFrame
     (send _prevFrame :deserialize buf ptr-) (incf ptr- (send _prevFrame :serialization-length))
   ;; sensor_msgs/Image _gray_frame
     (send _gray_frame :deserialize buf ptr-) (incf ptr- (send _gray_frame :serialization-length))
   ;;
   self)
  )

(setf (get motion_tracker::ImageContour :md5sum-) "ec56e43facaaa5042c6f1314b2415932")
(setf (get motion_tracker::ImageContour :datatype-) "motion_tracker/ImageContour")
(setf (get motion_tracker::ImageContour :definition-)
      "string ann_file
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

")



(provide :motion_tracker/ImageContour "ec56e43facaaa5042c6f1314b2415932")


