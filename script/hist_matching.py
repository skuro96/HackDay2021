#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""hist matching."""

import cv2
import os

def add_zeros(path_number):
    if (len(path_number) == 1):
        return '000' + path_number
    elif (len(path_number) == 2):
        return '00' + path_number
    elif (len(path_number) == 3):
        return '0' + path_number
    else:
        return path_number

# TARGET_FILE = 'train_0000.jpg'
IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/../data/temp/'
IMG_SIZE = (200, 200)
temp = 0

for i in range(6901):
    # print(i)
    j = i + 1
    i = str(i)
    j = str(j)
    i = add_zeros(i)
    j = add_zeros(j)

    target_img_path = IMG_DIR + 'train_' + i + '.jpg'
    target_img = cv2.imread(target_img_path)
    target_img = cv2.resize(target_img, IMG_SIZE)
    target_hist = cv2.calcHist([target_img], [0], None, [256], [0, 256])

    comparing_img_path = IMG_DIR + 'train_' + j + '.jpg'
    # print('FILE: %s : %s' % ('train_' + i + '.jpg', 'train_' + j + '.jpg'))
    comparing_img = cv2.imread(comparing_img_path)
    comparing_img = cv2.resize(comparing_img, IMG_SIZE)
    comparing_hist = cv2.calcHist([comparing_img], [0], None, [256], [0, 256])
    ret = cv2.compareHist(target_hist, comparing_hist, 0)
    # print(file, ret)
    print(ret - temp)
    temp = ret