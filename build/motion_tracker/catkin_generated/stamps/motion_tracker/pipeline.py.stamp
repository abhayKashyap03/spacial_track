#!/usr/bin/env python3
print(__package__)

import cv2
import rospy
import argparse
import pandas as pd
import otherVars as ov
from cv_bridge import CvBridge
from motion_tracker.msg import ImageContour
from sensor_msgs.msg import Image


def subscriber():
    rospy.init_node('motion_track', anonymous=True)
    rospy.Subscriber('/camera/image', Image, publish)
    rospy.spin()


def publish(data):
    prevFrame = ov.prevFrame
    pub = rospy.Publisher('motionTracking', ImageContour, queue_size=10)
    rate = rospy.Rate(10)
    br = CvBridge()
    print(data)

    while not rospy.is_shutdown():
        rospy.loginfo('Tracking Video')

        frame = br.imgmsg_to_cv2(data)
        cv2.imshow("frame", frame)
        if frame is None:
            break

        # frame = cv2.resize(frame, (640, 640))
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if prevFrame is None:
            prevFrame = gray_frame
            continue

        msg = ImageContour()
        # msg.ann_file = args.ann_file
        msg.frame = br.cv2_to_imgmsg(frame)
        msg.prevFrame = br.cv2_to_imgmsg(prevFrame)
        msg.gray_frame = br.cv2_to_imgmsg(gray_frame)
        pub.publish(msg)
        rate.sleep()
        rospy.loginfo('Tracked Video')


if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
