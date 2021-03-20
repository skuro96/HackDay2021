#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""feature detection."""

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

TARGET_FILE = '05.png'
IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/../data/temp/'
IMG_SIZE = (200, 200)
for i in range(6901):
    # print(i)
    j = i + 1
    i = str(i)
    j = str(j)
    i = add_zeros(i)
    j = add_zeros(j)

    target_img_path = IMG_DIR + 'train_' + i + '.jpg'
    target_img = cv2.imread(target_img_path, cv2.IMREAD_GRAYSCALE)
    target_img = cv2.resize(target_img, IMG_SIZE)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    # detector = cv2.ORB_create()
    detector = cv2.AKAZE_create()
    (target_kp, target_des) = detector.detectAndCompute(target_img, None)

    comparing_img_path = IMG_DIR +'train_' + j + '.jpg'
    print('FILE: %s - %s' % ('train_' + i + '.jpg', 'train_' + j + '.jpg'))
    try:
        comparing_img = cv2.imread(comparing_img_path, cv2.IMREAD_GRAYSCALE)
        comparing_img = cv2.resize(comparing_img, IMG_SIZE)
        (comparing_kp, comparing_des) = detector.detectAndCompute(comparing_img, None)
        matches = bf.match(target_des, comparing_des)
        dist = [m.distance for m in matches]
        ret = sum(dist) / len(dist)
    except cv2.error:
        ret = 100000

    print(ret)