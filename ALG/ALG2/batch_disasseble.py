# -*- coding: utf-8 -*-


import os
import subprocess

def disassemble(frompath, topath, num, start=0):
    files = os.listdir(frompath)
    files = files[start:num]
        
    total = len(files)
    
    for i, file in enumerate(files):
        fullFrompath = "\"" + os.path.join(frompath, file)+"\""
        fullTopath = "\""+ os.path.join(topath, file)+"\""

        # apktooldir = "/home/ubuntu/gexiuting-n-gram"
        command = "apktool d -f {0} -o {1}".format(fullFrompath, fullTopath)
        print("--- ",command)
        subprocess.call(command, shell=True)


if __name__ == "__main__":
    # 反汇编恶意软件样本
    virus_root = r'D:\Program Files\pycharm\AndroidMalwareWithN-gram-master\malware'
    disassemble(virus_root, r'D:\Program Files\pycharm\AndroidMalwareWithN-gram-master\smalis\malware',
                                 600)

    # 反汇编正常软件样本
    kind_root = r'D:\Program Files\pycharm\AndroidMalwareWithN-gram-master\benign'
    disassemble(kind_root, r'D:\Program Files\pycharm\AndroidMalwareWithN-gram-master\smalis\benign',
                                 600)
