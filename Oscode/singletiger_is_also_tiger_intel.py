import os
from shutil import copy as cp

dirs = os.listdir('/home/amurtiger/SingleTiger')
for dir in dirs:
    pics = os.listdir('/home/amurtiger/SingleTiger/' + dir)
    for pic in pics:
        pic_path = os.path.join('/home/amurtiger/SingleTiger/' + dir,pic)
        target_path = '/home/amurtiger/Tiger/MARSDATASET/pic_track_20191108/' + dir
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        cp(pic_path,target_path)