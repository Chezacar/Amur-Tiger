import numpy as np
import json
import PIL.Image as im
import numpy as np
import os
def processtxt(file):
    dataMat = []
    f = open(root + '/' + file)
    for line in f.readlines():
        lineArr = line.strip().split(',')
        #print(lineArr)
        dataMat.append(lineArr)
        #labelMat.append(float(lineArr[2]))
    return dataMat

def getfilename(file,suffix):
    serial = str(suffix)
    filename = file[:-4] + '_' + serial + '.txt'
    return filename

def writetrack(filename,content):
    output = open(filename,'a',encoding = 'UTF-8')
    #output.read()
    #content = str(content)
    x = content.shape[0]
    for i in range(0,x-1):
        output.write(str(content[i]))
        output.write(',')
    output.write(str(content[x-1]))
    #output.write(content)
    output.write('\n')
    output.close

for root,dirs,files in os.walk(r'G:/SJTU/1920fall/智能系统设计/sort2/output'):
    for file in files:
        data = processtxt(file)
        data = np.array(data)
        data = data.astype(np.float)
        data = np.round(data)
        data = data.astype(np.int)
        #data[:,1] = data[:,1].astype(np.int)
        #data[:,0] = data[:,0].astype(np.int)
        print(data.shape)
        print(data.dtype)
        x = data.shape[0]
        print(x)
        for i in range(0,x):
            #track_index = np.zeros((2,1))
            #track_index = []
            #if data[i,1] not in track_index:
                #temp = [[data[i,1]],[1]]
                #track_index.append(data[i,1])
                serial = str(data[i,1])
                filename = getfilename(file,data[i,1])
                writetrack(filename,data[i,:])
                #np.savetxt(filename,data[i,:],delimiter = ',')
            #else:
            #    temp1 = np.where(track_index[0,:] == data[i,1])[0]
            