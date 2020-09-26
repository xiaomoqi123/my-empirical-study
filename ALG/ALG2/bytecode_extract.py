# -*- coding: utf-8 -*-


from infrastructure.ware import Ware
from infrastructure.fileutils import DataFile

virusroot = "./smalis/malware"
kindroot = "./smalis/benign"


import os

def collect(rootdir, isMalware,f):

    wares = os.listdir(rootdir)
    total = len(wares)
    for i, ware in enumerate(wares):
        warePath = os.path.join(rootdir, ware)
        ware = Ware(warePath, isMalware)
        ware.extractFeature(f)
        print("已提取", i + 1, "个文件的特征，百分比如下：")
        print((i + 1) * 100 / total, "%")


if __name__ == "__main__":
    #1代表恶意软件
    f = DataFile("./result/data.csv")
    collect(virusroot, 1,f)
    collect(kindroot, 0,f)
    f.close()





