import pandas as pd
import argparse
import cv2
import glob
import os
from natsort import natsorted


def find_iou(box1, box2):
    if all(box1 == 0) and all(box2 == 0):
        return 0

    x1, y1, x2, y2 = box1
    x3, y3, x4, y4 = box2

    intersection_width = max(min(x2, x4) - max(x1, x3), 0)
    intersection_height = max(min(y2, y4) - max(y1, y3), 0)

    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x4 - x3) * (y4 - y3)

    intersection_area = abs(intersection_height * intersection_width)
    union_area = abs(box1_area) + abs(box2_area) - intersection_area
    iou = intersection_area / union_area

    return iou


def max_area_box(df):
    for i in range(len(df)-1):
        if i not in df.index:
            continue
        row1 = df.loc[i]
        row2 = df.loc[i+1]
        if row1.image == row2.image:
            area1 = abs((row1.xmax-row1.xmin) * (row1.ymax-row1.ymin))
            area2 = abs((row2.xmax - row2.xmin) * (row2.ymax - row2.ymin))

            if area1 > area2:
                df = df.drop(index=i+1)
            else:
                df = df.drop(index=i)
    return df


class CompareBoxes:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--ground_truth', '-gt', help='User annotations CSV')
        parser.add_argument('--alg_pred', '-ap', help='CSV with predictions by algorithm')
        parser.add_argument('--video')
        parser.add_argument('--frames_folder', '-ff')
        args = parser.parse_args()
        self.gt_df = pd.read_csv(args.ground_truth)
        self.ap_df = max_area_box(pd.read_csv(args.alg_pred))
        self.len = int(cv2.VideoCapture(args.video).get(cv2.CAP_PROP_FRAME_COUNT))
        self.frames_folder = args.frames_folder

    def fill_df(self, df):
        if 'speed' in df.columns:
            df = pd.DataFrame({'image': df.image, 'xmin': df.xmin, 'ymin': df.ymin, 'xmax': df.xmax, 'ymax': df.ymax, 'speed': df.speed})
        else:
            df = pd.DataFrame({'image': df.image, 'xmin': df.xmin, 'ymin': df.ymin, 'xmax': df.xmax, 'ymax': df.ymax})
        index = df.index
        df['image'] = [int(i[5:]) for i in df['image'].to_numpy()]
        df.sort_values('image', inplace=True)
        df.index = index

        for i in range(1, self.len+1):
            if i not in df.image.to_numpy():
                df = df.append({'image': int(i)}, ignore_index=True)
        index = df.index
        df.sort_values('image', inplace=True)
        df.index = index
        df = df.fillna(0)

        return df

    def compare_boxes(self):
        gt_df = self.fill_df(self.gt_df)
        ap_df = self.fill_df(self.ap_df)

        all_iou = []
        cols = ['xmin', 'ymin', 'xmax', 'ymax']

        for i in range(len(gt_df)):
            box1 = gt_df.iloc[i][cols].to_numpy()
            box2 = ap_df.iloc[i][cols].to_numpy()
            all_iou.append(find_iou(box1, box2))

        # print(all_iou)
        avg_iou = sum(all_iou) / len(all_iou)
        avg_speed = self.ap_df['speed'].to_numpy()[-1]/len(self.ap_df)
        print('Average Accuracy : {} %\nAverage Speed per Frame : {} ms'.format(round(avg_iou*100, 2),
                                                                            round(avg_speed*1000, 2)))

    def draw_boxes(self):
        files = natsorted(glob.glob(os.path.join(self.frames_folder, '*.jpg')))
        imgs = []
        for file in files:
            imgs.append(cv2.imread(file))

        for i in range(len(imgs)):
            x1, y1, x2, y2 = self.gt_df[['xmin', 'ymin', 'xmax', 'ymax']].iloc[i]
            x3, y3, x4, y4 = self.ap_df[['xmin', 'ymin', 'xmax', 'ymax']].iloc[i]
            cv2.rectangle(imgs[i], (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.rectangle(imgs[i], (int(x3), int(y3)), (int(x4), int(y4)), (255, 0, 0), 2)

            cv2.imshow('frame', imgs[i])
            cv2.waitKey(200)

        cv2.destroyAllWindows()


cb = CompareBoxes()
# cb.draw_boxes()
cb.compare_boxes()
