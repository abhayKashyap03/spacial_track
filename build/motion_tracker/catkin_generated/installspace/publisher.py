import cv2
import rospy
import os
import argparse
import pandas as pd
from cv_bridge import CvBridge
from motion_tracker.msg import ImageContour


parser = argparse.ArgumentParser()
parser.add_argument('--video', '-v', type=str)
parser.add_argument('--ann_file', '-af', type=str)
args = parser.parse_args()


def publisher():
    pub = rospy.Publisher('motionTracking', ImageContour, queue_size=10)
    rospy.init_node('motion_track', anonymous=True)
    rate = rospy.Rate(10)

    br = CvBridge()
    if os.path.isfile(args.ann_file):
        boxes = pd.read_csv(args.ann_file)
        boxes.iloc[0:0].to_csv(args.ann_file, index=False)
    else:
        boxes = pd.DataFrame(columns=['image', 'xmin', 'ymin', 'xmax', 'ymax', 'speed'])
        boxes.to_csv(args.ann_file, index=False)

    vid = cv2.VideoCapture(args.video)
    firstFrame = None
    while not rospy.is_shutdown():
        rospy.loginfo('Tracking Video')

        ret, frame = vid.read()
        if frame is None:
            break

        # frame = cv2.resize(frame, (640, 640))
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if firstFrame is None:
            firstFrame = gray_frame
            continue

        msg = ImageContour()
        msg.ann_file = args.ann_file
        msg.frame = br.cv2_to_imgmsg(frame)
        msg.firstFrame = br.cv2_to_imgmsg(firstFrame)
        msg.gray_frame = br.cv2_to_imgmsg(gray_frame)
        pub.publish(msg)
        rate.sleep()
        rospy.loginfo('Tracked Video')


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
