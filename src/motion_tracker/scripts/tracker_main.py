#!/usr/bin/env python

import rospy
import cv2
import sys
import argparse
import os

import numpy as np
import pcl3d.pcl_process as pcl_p
import bbox2d.img_process as img_p
import optical_flow

from sensor_msgs.msg import LaserScan, CompressedImage, CameraInfo
from sensor_msgs import point_cloud2 as pc2
from message_filters import Subscriber, ApproximateTimeSynchronizer
import laser_geometry.laser_geometry as lg
from image_geometry import PinholeCameraModel as phcm
from time import time

sys.path.append('/scripts/')


def get_object_info(ci_msg, bbox, pc):
    x, y, w, h = bbox
    loc_x, loc_y = (x + (w / 2)), (y + h)

    img_proc = phcm()
    img_proc.fromCameraInfo(ci_msg)

    pixel3d = img_proc.projectPixelTo3dRay((loc_x, loc_y))
    pixel3d_normalized = np.array(pixel3d) / pixel3d[-1]
    pixel3d_norm = np.linalg.norm(pixel3d_normalized)

    direction = np.arcsin(pixel3d_normalized[1] / pixel3d_norm)
    direction = 180 * direction / np.pi

    direction = direction*-1 if pixel3d_normalized[0] < 0 else direction
    dir_range = [345 - direction, 345 + direction if (direction+360) > 345 else 360]
    dist_range = pc.to_ndarray()[np.logical_and(dir_range[0] < pc['index'],
                                                pc['index'] < dir_range[1])]
    if len(dist_range) <= 3:
        distance = np.nan
    else:
        distance = round(np.sqrt(np.mean(dist_range['x']) ** 2 + np.mean(dist_range['y']) ** 2), 2)

    """
    distance : norm(pixel3d) = height : norm(vector_h)
    
    height = distance * norm(vector_h) / norm(pixel3d)
    
    vector_h --> { vector from (loc_x, loc_y, 1) to (loc_x, y, 1) } or 
                 { vector diff between pixel3d_normalized and 3d vector to (loc_x, y) }
    """

    top_pixel3d = img_proc.projectPixelTo3dRay((loc_x, y))
    top_pixel3d_normalized = np.array(top_pixel3d) / top_pixel3d[-1]

    __cos_theta = np.clip(np.dot(pixel3d_normalized, top_pixel3d_normalized), -1.0, 1.0)

    top_pixel3d_norm = np.linalg.norm(top_pixel3d_normalized)

    vector_h = (top_pixel3d_norm**2) + (pixel3d_norm**2) - (2*top_pixel3d_norm*pixel3d_norm*__cos_theta)

    height = distance * vector_h / pixel3d_norm

    print("Height: ", height, vector_h, pixel3d_norm, "\n\n")

    return distance, height, direction


class MainTracker:
    def __init__(self, publish_pcl=True, bbox_doc=False, ann_file=None):
        print('%s Starting Motion Tracker %s\n' % ('-' * 10, '-' * 10))
        self.start = time()
        self.count = 1
        self.prev_dist = 0

        scan_sub = Subscriber('/scan', LaserScan)
        img_sub = Subscriber('/camera/image/compressed', CompressedImage)
        c_i = Subscriber('/camera/camera_info', CameraInfo)
        ts = ApproximateTimeSynchronizer([img_sub, scan_sub, c_i], 1, 0.5)
        ts.registerCallback(self.track)
        self.pc_process = pcl_p.PCLProcess(publish=publish_pcl)
        self.img_process = img_p.IMGProcess(bbox_doc=bbox_doc, ann_file=ann_file)
        self.optical_flow = optical_flow.Estimator

    def preprocess(self, img_msg, scan_msg, ci_msg):
        frame = self.img_process.preprocess(img_msg, ci_msg)
        pc = self.pc_process.preprocess(scan_msg)
        return frame, pc

    def track(self, img_msg, scan_msg, ci_msg):
        print('Tracking Moving Objects...')

        frame, pc = self.preprocess(img_msg, scan_msg, ci_msg)

        bboxes = self.img_process.get_bboxes(frame)

        if bboxes:
            img_p.draw_bbox(frame, bboxes)
            for bbox in bboxes:
                distance, height, direction = get_object_info(ci_msg, bbox, pc)
                if distance is np.nan:
                    distance = self.prev_dist
                if direction > 0:
                    obj_dir = "%.2f degrees to the right" % (np.abs(direction))
                elif direction < 0:
                    obj_dir = "%.2f degrees to the left" % (np.abs(direction))
                else:
                    obj_dir = "in front of the camera"
                self.prev_dist = distance

            if self.count > 1 and self.count % 25 == 0:
                print("\n\n%s\nObject of height %.2fm is %.2fm away %s\n%s\n\n" % ('-' * 20, height, distance, obj_dir, '-' * 20))

        if self.count == 1:
            self.optical_flow(frame)
        else:
            self.optical_flow.run(frame, bboxes)

        self.count += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bbox_doc', '-bdoc', choices=[True, False], default=False)
    parser.add_argument('--publish_pcl', choices=[True, False], default=False)
    args = parser.parse_args()
    ann_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pred_bbox_ann.csv") if args.bbox_doc else None
    rospy.init_node('motion_tracker', anonymous=True)
    MainTracker(args.publish_pcl, args.bbox_doc, ann_file)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        exit(0)
