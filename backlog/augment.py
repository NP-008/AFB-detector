# augment image to 6 times

import cv2
import os
import numpy as np

def flip_h(img):
    flipped_img = np.fliplr(img)
    return flipped_img

def flip_v(img):
    flipped_img = np.flipud(img)
    return flipped_img

def rotate(img, degree):
    img = np.array(img)
    if degree == 90:
        rotated_img = np.rot90(img, k=1)
    elif degree == 180:
        rotated_img = np.rot90(img, k=2)
    elif degree == 270:
        rotated_img = np.rot90(img, k=3)
    return rotated_img

for i in os.listdir('~/forenterbook/train/positive/'):
    img = cv2.imread('~/forenterbook/train/positive/' + i)
    img = np.array(img)
    aug_path = '~/forenterbook/train/augment'
    img_name = i.replace('.jpeg', 'fv.jpeg')
    cv2.imwrite(os.path.join(aug_path, img_name), flip_v(img))
    img_name = i.replace('.jpeg', 'fh.jpeg')
    cv2.imwrite(os.path.join(aug_path, img_name), flip_h(img))
    img_name = i.replace('.jpeg', 'r.jpeg')
    cv2.imwrite(os.path.join(aug_path, img_name), rotate(img, 90))
    img_name = i.replace('.jpeg', 'rr.jpeg')
    cv2.imwrite(os.path.join(aug_path, img_name), rotate(img, 180))
    img_name = i.replace('.jpeg', 'rrr.jpeg')
    cv2.imwrite(os.path.join(aug_path, img_name), rotate(img, 270))
    print(i)
