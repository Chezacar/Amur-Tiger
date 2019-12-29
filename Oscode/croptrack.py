import numpy as np
import os 
import PIL.Image as im

def processtxt(file):
    dataMat = []
    f = open(root + '/' + file)
    for line in f.readlines():
        lineArr = line.rstrip('\n').split(',')
        #print(lineArr)
        dataMat.append(lineArr)
        #labelMat.append(float(lineArr[2]))
    return dataMat

for root,dirs,files in os.walk(r"G:/SJTU/1920fall/智能系统设计/sort2/divide_with_track"):
        for file in files:
            dirs2 = os.listdir("G:/SJTU/1920fall/智能系统设计/sort2/mot_benchmark/train")
            for dir2 in dirs2:
                if (file[:6] == dir2[:6]):
                    #datamat = []
                    #filepath = 'G:/SJTU/1920fall/智能系统设计/sort2/divide_with_track/' + file
                    #datamat = np.loadtxt(filepath)
                    #track_size = datamat.shape(0)
                    datamat = processtxt(file)
                    print(len(datamat))
                    track_size = len(datamat)
                    datamat = np.array(datamat)
                    datamat = datamat.astype(np.int)
                     #datamat =datamat.reshape((track_size,10))
                    picpath = 'G:/SJTU/1920fall/智能系统设计/sort2/mot_benchmark/train/' + dir2 + '/img1'
                    pics = os.listdir(picpath)
                    #print(datamat.shape)
                    #track_size = datamat.shape[0]
                    for i in range(0,track_size):
                        crop_district = (datamat[i,2],datamat[i,3]\
                            ,datamat[i,2] + datamat[i,4]\
                                ,datamat[i,3] + datamat[i,5])
                        for pic in pics: 
                            pic_index = pic.lstrip('0').rstrip('.jpg')
                            if str(datamat[i][0]) == pic_index:
                                image = im.open(picpath + '/' + pic)
                                image_crop = image.crop(crop_district)
                                output_pic_name = file[:-4] + '_' + str(datamat[i,0]) + '.jpg'
                                pic_path = os.path.join('G:/SJTU/1920fall/智能系统设计/sort2/pic_crop_with_track',file[:-4])
                                pic_name = os.path.join('G:/SJTU/1920fall/智能系统设计/sort2/pic_crop_with_track',file[:-4],output_pic_name)
                                if not os.path.exists(pic_path):
                                    os.makedirs(pic_path)
                                outputpath = os.path.join(pic_name)
                                image_crop.save(outputpath)
                