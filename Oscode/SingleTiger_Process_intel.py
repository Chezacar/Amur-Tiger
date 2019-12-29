import numpy as np
import os
from shutil import copy as cp

def whetherone(picname,findpath):
    files = os.listdir(findpath)
    flag = 1
    picname_title = picname[:-9]
    for file in files:
        filename = file[:-11]    
        if filename == picname_title and file[-5] == '2':
            flag = 0
            break    
    return flag

pics = os.listdir('/home/amurtiger/allPics')
i = 0
for pic in pics:
    Flag = whetherone(pic,'/home/amurtiger/Crop')
    print(Flag)
    if Flag:
        pic_track = os.listdir('/home/amurtiger/Crop')
        for temp in pic_track:
            if temp == (pic[:-4] + '_1' + '.jpg'):
                pic_path = '/home/amurtiger/SingleTiger/' + pic[0:pic.find('_')]
                if not os.path.exists(pic_path):
                    os.makedirs(pic_path)
                cp(temp,pic_path)
    i += 1
    print(i)