#coding=utf-8
from PIL import Image
import numpy as np
import sys
import os
import cv2
if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    height =int(sys.argv[3])
    width =int(sys.argv[4])
    blurKsize=int(sys.argv[5])

    img=cv2.imread(in_file)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.equalizeHist(img)
    img=cv2.GaussianBlur(img,(blurKsize,blurKsize),0)
    img=cv2.resize(img,(width*2, height*3))
    #cv2.imwrite('gray.jpg',img)
    th,img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    #cv2.imwrite('binary.jpg',img)
    img=img/255
    ch =np.array([' ', '⠁', '⠂', '⠃', '⠄', '⠅', '⠆', '⠇', '⠈', '⠉', '⠊', '⠋', '⠌', '⠍', '⠎', '⠏', '⠐', '⠑', '⠒', '⠓', '⠔', '⠕',
         '⠖', '⠗', '⠘', '⠙', '⠚', '⠛', '⠜', '⠝', '⠞', '⠟', '⠠', '⠡', '⠢', '⠣', '⠤', '⠥', '⠦', '⠧', '⠨', '⠩', '⠪', '⠫',
         '⠬', '⠭', '⠮', '⠯', '⠰', '⠱', '⠲', '⠳', '⠴', '⠵', '⠶', '⠷', '⠸', '⠹', '⠺', '⠻', '⠼', '⠽', '⠾', '⠿','\n'],np.str)
    img=img[0::3,0::2]+img[1::3,0::2]*2+img[2::3,0::2]*4+img[0::3,1::2]*8+img[1::3,1::2]*16+img[2::3,1::2]*32
    img=np.insert(img,width,64,-1)
    img=np.array(img,np.int)
    res=ch[img]
    res=np.reshape(res,(-1))

    with open(out_file,'w',encoding='utf-8')as f:
        f.writelines(res)
