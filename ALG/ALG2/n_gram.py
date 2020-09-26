# -*- coding: utf-8 -*-

import sys,os,shutil
from infrastructure.ware import Ware
from infrastructure.fileutils import DataFile
import pandas as pd
import bytecode_extract as be
import batch_disasseble as bd
from infrastructure.mydict import MyDict


# #反汇编恶意软件样本
# malware_path = "./apk/malware"
# if not os.path.exists("./smalis/malware"):
#     os.mkdir("./smalis/malware")
# malware_root = "./smalis/malware"
# bd.disassemble(malware_path, malware_root, 5000)
#
# # 反汇编正常软件样本
# benign_path = "./apk/benign"
# if not os.path.exists("./smalis/benign"):
#     os.mkdir("./smalis/benign")
# benign_root = "./smalis/benign"
# bd.disassemble(benign_path, benign_root, 5000)
#
# f = DataFile("./result/data.csv")
# be.collect(malware_root, 1, f)
# be.collect(benign_root, 0, f)
# f.close()

n = 4
mdict = MyDict()
origin = pd.read_csv("./result/data.csv")
feature = origin["Feature"].str.split("|")
label = origin["isMalware"]

total = len(feature)
for i, code in enumerate(feature):#i代表下标，code代表feature中的值
    mdict.newLayer()
    if not type(code) == list:
        continue
    for method in code:
        length = len(method)
        if length < n:
            continue
        for start in range(length - (n - 1)):
            end = start + n
            mdict.mark(method[start:end])

result = mdict.dict
pd.DataFrame(result, index=origin.index) .to_csv("./result/" + str(n) + "_gram.csv", index=False)


if os.path.exists(malware_root):
    shutil.rmtree(malware_root)
if os.path.exists(benign_root):
    shutil.rmtree(benign_root)
        


