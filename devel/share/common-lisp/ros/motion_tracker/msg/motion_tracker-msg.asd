
(cl:in-package :asdf)

(defsystem "motion_tracker-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "ImageContour" :depends-on ("_package_ImageContour"))
    (:file "_package_ImageContour" :depends-on ("_package"))
  ))