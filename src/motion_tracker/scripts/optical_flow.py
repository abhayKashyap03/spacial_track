import cv2
import numpy as np
import bbox2d.img_process as img_p


class Estimator:
    def __init__(self, init_img):
        self.prev_image = init_img
        self.hsv_mask = np.zeros_like(init_img)
        self.hsv_mask[..., 1] = 255

    def run(self, image, bbox=None):
        prev_gray = cv2.cvtColor(self.prev_image, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray_img, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        # Set image hue value according to the angle of optical flow
        hsv_mask[..., 0] = ang * 180 / np.pi / 2
        # Set value as per the normalized magnitude of optical flow
        hsv_mask[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

        rgb_representation = cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)
        img = cv2.bitwise_and(image, rgb_representation)

        if bbox is not None or bbox != []:
            img_p.draw_bbox(img, bbox)

        self.prev_image = image
