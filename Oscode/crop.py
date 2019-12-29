import json
import PIL.Image as im
import numpy as np
import os
with open("G:/SJTU/1920fall/智能系统设计/results.json",'r',encoding = 'UTF-8') as load_f:
     load_dict = json.load(load_f)

y = 0
for x in load_dict:
    y += 1
print(y)

useful = []
for i in range(0,y,1):
    #print(y)
    #print(y/100)
    if load_dict[i]['bbox'][1] != 0:
        useful.append(load_dict[i])

j = 0
for i in useful:
    j += 1 
    #print(i)
print(j)

t = 1
for i in useful:
    #print(i['image_id'])
    temp = useful.index(i)
    if i['image_id'] == useful[temp-1]['image_id']:
        t += 1
    else:
        t = 1
    target = i['image_id'] + '.jpg'
    #print(target)
    for root,dirs,files in os.walk(r"G:\SJTU\1920fall\智能系统设计\VOC\JPEGImages"):
        for file in files:
            if file == target:
                path  = os.path.join(root,file)
                break
    x = im.open(path)
    cropparm = np.int()
    cropparm = np.array((i['bbox'][0],i['bbox'][1],i['bbox'][0] + i['bbox'][2],i['bbox'][1] + i['bbox'][3]))
    cropparm = cropparm.astype(int)
    #print(cropparm)
    imout = x.crop(cropparm)
    temp1 = str(t)
    #print(temp1)
    #temp = 'G:\SJTU\1920fall\智能系统设计\VOC\JPEGImages/'
    outputpath = i['image_id']+ '_' + temp1 + '.jpg'
    print(outputpath)
    imout.save(outputpath)