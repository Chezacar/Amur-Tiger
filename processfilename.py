import os
import numpy

path = './python-ECO-HC-master/sequences/Tiger_35/img/'
filenames = os.listdir(path)
for file in filenames:
    num = file[7:11]
    print(file[7:11])
    num_int = int(num) - 1511
    temp = '0000' + str(num_int)
    print(temp)
    print(temp[-4:])
    new_name = temp[-4:] + '.jpg'
    os.rename(path + file,path + new_name)