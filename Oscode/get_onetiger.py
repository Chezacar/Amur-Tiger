"""1
这段函数根据Crop中图片的名称筛选出allPics中只有单个老虎的图片
结果仍然保存在allPics中
"""
import os

roota = './Crop/'
rootb = './allPics/'


def test1(root):
    qian = ''
    ifde = False  # ifde代表以此前缀开头的图片是否删除
    for file in os.listdir(root):
        qian2 = file.split('e')[-2]  # 用e分割取前缀
        if qian != qian2:
            if ifde:  # 删除以qian开头的图片
                deltiger(rootb, qian)
                ifde = False
            qian = qian2  # 这一行也总是忘记写
            print(qian)
        else:
            if not ifde:  # 根据tigerid来看是否删除
                tigerid2 = file.split('.')[-2]
                tigerid = tigerid2.split('_')[-1]
                if tigerid != '1':
                    ifde = True
            else:  # 如果确定删则以此前缀开头的图片都不用再看
                continue
    if ifde:
        deltiger(rootb, qian)


def deltiger(root, qian):
    """
    :param root: 图片所在的文件夹
    :param qian: 要删除的图片的前缀
    :return: 无
    """
    print('del')
    for file in os.listdir(root):
        qian2 = file.split('e')[-2]
        if qian == qian2:
            os.remove(root + file)


def delnoid(root):  # 删除以noid开头的图片
    qian = 'noID'
    for file in os.listdir(root):
        qian2 = file.split('_')[0]
        if qian == qian2:
            os.remove(root + file)


test1(roota)
delnoid(rootb)
