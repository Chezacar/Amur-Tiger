import pickle
import numpy as np
import os
import PIL.Image as im
with open('./box.pkl','rb') as f:
    data = pickle.load(f,encoding = 'bytes')
for key in data:
    print(key)
    for i in data[key]:
        for j in data[key][i]:
            arr1 = [int(val) for val in j]
            kuang = arr1[1:]
            frame = '000000' + str(arr1[0])
            frame = frame[-5:]
            pic_dir = '000000' + str(i)
            pic_dir = pic_dir[-5:]
            pic_name = 'image' + '_' + frame + '.jpg'
            #print(pic_name)
            #print(pic_dir)
            dirs = os.listdir('/home/amurtiger/Tiger/video')
            for dir in dirs:
                if dir == pic_dir:
                    lujing = '/home/amurtiger/Tiger/video/' + dir
                    files = os.listdir(lujing)
                    for file in files:
                        if file == pic_name:
                            path = os.path.join(lujing,file)
                            break
            x = im.open(path)
            cropparm = np.int()
            cropparm = np.array((kuang[0],kuang[1],kuang[2],kuang[3]))
            cropparm = cropparm.astype(int)
            imout = x.crop(cropparm)
            outputpath = str(key) + '_' + str(i) + '_' + pic_name
            print(outputpath)
            imout.save(outputpath)
