import os
import cv2
import json
import rospy
import imutils
import argparse

import numpy as np
import pandas as pd

from time import time
from cv_bridge import CvBridge


def draw_bbox(frame, bboxes):
    frame_copy = frame.copy()
    print(bboxes)
    for bbox in bboxes:
        x, y, w, h = bbox
        cv2.rectangle(frame_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("frame", frame_copy)
    cv2.waitKey(200000)


def evaluate(video, ground_truth):
    truth_bboxes_paths = {round(json.load(open(os.path.join(ground_truth, x)))['asset']['timestamp'], 2): os.path.join(ground_truth, x)
                          for x in os.listdir(ground_truth) if x.endswith(".json")}
    truth_bboxes_paths = {k: truth_bboxes_paths[k] for k in sorted(truth_bboxes_paths.keys())}

    cap = cv2.VideoCapture(video)
    ret, frame = cap.read()

    img_proc = IMGProcess()
    img_proc.prev_frame = img_proc.get_gray_img(frame)

    good, count = 0, 0
    while ret:
        ret, frame = cap.read()
        if not ret:
            break

        time_frame = round(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000, 2)

        if time_frame in truth_bboxes_paths.keys() or time_frame+0.01 in truth_bboxes_paths.keys() \
                or time_frame-0.01 in truth_bboxes_paths.keys():
            box_pred = img_proc.get_bboxes(frame)

            if box_pred is not None and box_pred != []:
                area, biggest_box = 0, []
                for box in box_pred:
                    box = (box[0], box[1], box[0]+box[2], box[1]+box[3])
                    box_ar = (box[2] - box[0]) * (box[3] - box[1])
                    if box_ar >= area:
                        area = box_ar
                        biggest_box = box

                try:
                    points = json.load(open(truth_bboxes_paths[time_frame]))['regions'][0]['points']
                except KeyError:
                    points = json.load(open(truth_bboxes_paths[time_frame-0.01]))['regions'][0]['points']
                except KeyError:
                    points = json.load(open(truth_bboxes_paths[time_frame+0.01]))['regions'][0]['points']

                box_truth = [points[0]['x'], points[0]['y'], points[2]['x'], points[2]['y']]

                x1, y1, x2, y2 = biggest_box
                x3, y3, x4, y4 = box_truth

                intersection_width = max(min(x2, x4) - max(x1, x3), 0)
                intersection_height = max(min(y2, y4) - max(y1, y3), 0)

                box1_area = (x2 - x1) * (y2 - y1)
                box2_area = (x4 - x3) * (y4 - y3)

                intersection_area = abs(intersection_height * intersection_width)
                union_area = abs(box1_area) + abs(box2_area) - intersection_area
                if intersection_area/union_area >= 0.5:
                    good += 1

            count += 1

    return "AP @ IoU=0.5: " + str(round(good*100/count, 2))+"%"


class IMGProcess:
    def __init__(self, bbox_doc=False, ann_file=None):
        self.bbox_doc = bbox_doc
        self.ann_file = ann_file
        if self.bbox_doc:
            if os.path.isfile(self.ann_file):
                self.boxes = pd.read_csv(self.ann_file)
                self.boxes.iloc[0:0].to_csv(self.ann_file, index=False)
            else:
                self.boxes = pd.DataFrame(columns=['image', 'xmin', 'ymin', 'xmax', 'ymax', 'speed'])
                self.boxes.to_csv(self.ann_file, index=False)

        self.start = time()
        # self.br = CvBridge()
        self.prev_frame = None

    def preprocess(self, img_msg, ci_msg):
        np_arr = np.fromstring(img_msg.data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if frame is None:
            return None
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        frame = self.__undistort(frame, ci_msg)
        return frame

    def __undistort(self, frame, ci_msg):
        h, w = frame.shape[:2]
        K, D = np.array(ci_msg.K).reshape(3, 3), np.array(ci_msg.D)
        new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(K, D, (h, w), 0, (h, w))
        mapX, mapY = cv2.initUndistortRectifyMap(K, D, None, new_camera_mtx, (h, w), 5)
        img = cv2.remap(frame, mapX, mapY, cv2.INTER_LINEAR)
        return img

    def get_gray_img(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self.prev_frame is None:
            self.prev_frame = gray_frame
            return None
        return gray_frame

    def __get_biggest_bboxes(self, contours):
        bboxes = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area < 5000:
                continue
            bboxes.append(cv2.boundingRect(contour))
        return bboxes

    def __bbox_doc(self, bboxes):
        if self.boxes.image.empty:
            i = 1
        else:
            i = int(self.boxes.image.to_numpy()[-1][5:]) + 1

        for bbox in bboxes:
            x, y, w, h = bbox
            self.boxes = self.boxes.append({'image': 'frame' + str(i), 'xmin': x, 'ymin': y, 'xmax': x + w, 'ymax': y + h,
                                            'speed': time() - self.start}, ignore_index=True)
            self.boxes.to_csv(self.ann_file, index=False)

    def get_bboxes(self, frame):
        gray_frame = self.get_gray_img(frame)
        if frame is None or self.prev_frame is None or gray_frame is None:
            return

        diff = cv2.absdiff(self.prev_frame, gray_frame)
        threshold = cv2.threshold(diff, 70, 255, cv2.THRESH_BINARY)[1]
        threshold = cv2.dilate(threshold, None, iterations=2)
        contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)

        bboxes = self.__get_biggest_bboxes(contours)
        self.prev_frame = gray_frame

        if self.bbox_doc:
            self.bbox_doc(bboxes)

        return bboxes


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--evaluate', default=False, type=bool)
    parser.add_argument('--video', required=False)
    parser.add_argument('--ground_truth', required=False)
    arg = parser.parse_args()
    if arg.evaluate:
        print(evaluate(arg.video, arg.ground_truth))
        exit(0)
    else:
        IMGProcess()
    rospy.init_node('subscriber', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        exit(0)
