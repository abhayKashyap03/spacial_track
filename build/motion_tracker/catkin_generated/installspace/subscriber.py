#!/usr/bin/env python3

import rospy
import cv2
import imutils
import pandas as pd
from time import time
from motion_tracker.msg import ImageContour
from cv_bridge import CvBridge


start = time()


def motion_track(data):
    br = CvBridge()
    frame, prevFrame, grayFrame = br.imgmsg_to_cv2(data.frame), br.imgmsg_to_cv2(data.firstFrame), \
                                  br.imgmsg_to_cv2(data.gray_frame)
    diff = cv2.absdiff(prevFrame, grayFrame)
    cv2.imshow('diff', diff)

    threshold = cv2.threshold(diff, 89, 255, cv2.THRESH_BINARY)[1]

    threshold = cv2.dilate(threshold, None, iterations=2)
    contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    draw_rect([frame, contours])


def draw_rect(data):
    frame, contours = data

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 2000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    cv2.waitKey(2)


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' Data received!')
    motion_track(data)
    rospy.loginfo(rospy.get_caller_id() + ' Motion tracked!')


def subscriber():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('motionTracking', ImageContour, motion_track)
    rospy.spin()


if __name__ == '__main__':
    subscriber()
