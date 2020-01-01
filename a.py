#coding=utf-8
from PIL import Image
import numpy as np
import sys
import os

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    height =int(sys.argv[3])
    width =int(sys.argv[4])

    img = Image.open(in_file)
    img = img.convert('1')
    img = img.resize((width*2, height*3), Image.ANTIALIAS)
    img = np.asarray(img)

    ch =np.array([' ', '⠁', '⠂', '⠃', '⠄', '⠅', '⠆', '⠇', '⠈', '⠉', '⠊', '⠋', '⠌', '⠍', '⠎', '⠏', '⠐', '⠑', '⠒', '⠓', '⠔', '⠕',
         '⠖', '⠗', '⠘', '⠙', '⠚', '⠛', '⠜', '⠝', '⠞', '⠟', '⠠', '⠡', '⠢', '⠣', '⠤', '⠥', '⠦', '⠧', '⠨', '⠩', '⠪', '⠫',
         '⠬', '⠭', '⠮', '⠯', '⠰', '⠱', '⠲', '⠳', '⠴', '⠵', '⠶', '⠷', '⠸', '⠹', '⠺', '⠻', '⠼', '⠽', '⠾', '⠿','\n'],np.str)
    img=img[0::3,0::2]+img[1::3,0::2]*2+img[2::3,0::2]*4+img[0::3,1::2]*8+img[1::3,1::2]*16+img[2::3,1::2]*32
    img=63-img
    img=np.insert(img,width,64,-1)
    res=ch[img]
    res=np.reshape(res,(-1))

    with open(out_file,'w',encoding='utf-8')as f:
        f.writelines(res)
