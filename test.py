#coding=utf-8
from PIL import Image
import numpy as np
import sys
import os
import cv2
a=[bytearray(b'\xe2\xa0\x80'),bytearray(b'\xe2\xa1\x80'),bytearray(b'\xe2\xa2\x80'),bytearray(b'\xe2\xa3\x80')]
for i in range(256):
    d3=(i&8)>>3
    d7=(i&128)>>7
    d46=(i&112)>>1
    d02=(i&7)
    idx1=d46+d02
    idx2=(d7<<1)+d3
    b=a[idx2].copy()
    b[2]+=idx1
    print('\'{:}\''.format(str(b,encoding='utf-8')),end=',')