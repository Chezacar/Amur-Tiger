import numpy as np
import os
from shutil import copy as cp

def processtxt(file):
    dataMat = []
    f = open(file)
    for line in f.readlines():
        lineArr = line.strip().split(',')
        #print(lineArr)
        dataMat.append(lineArr)
        #labelMat.append(float(lineArr[2]))
    return dataMat



track = np.loadtxt('/home/amurtiger/Tiger/MARSDATASET/eff_trajs.txt')
track = track.astype(np.int)
files = files = os.listdir('/home/amurtiger/Tiger/MARSDATASET/output')
listoftrack = []
#    listoftrack.append(temp)
for track_index in track:
    for file in files:
        txtpath = '/home/amurtiger/Tiger/MARSDATASET/output/' + file
        temp = processtxt(txtpath)
        for pic in temp:
            track_index_str = str(track_index)
            if track_index_str == pic[1]:
                pic_path = '/home/amurtiger/Tiger/MARSDATASET/pic_crop_with_track/' + file[:-4] + '_' + track_index_str
                target_path = '/home/amurtiger/Tiger/MARSDATASET/pic_track_20191108/' + file[:file.find('_')] 
                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                if file[:3] != 'MOT':
                    pics = os.listdir(pic_path)
                    for biss in pics:
                        nm = pic_path + '/' + biss
                        cp(nm,target_path)