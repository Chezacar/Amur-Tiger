import json
import PIL.Image as im
import numpy as np
import os
piclist = []
picrange = []
output = open('piclist.txt','w',encoding = 'UTF-8')
for root,dirs,files in os.walk(r"G:/SJTU/1920fall/智能系统设计/sort2/mot_benchmark/train"):
    for file in files:
        piclist.append(file)
for pic in piclist:
    output.write(str(pic))
    output.write('\n')
    output.close

