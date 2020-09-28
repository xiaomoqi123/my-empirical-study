# -*- coding: utf-8 -*-


import requests
import os
import urllib
from bs4 import BeautifulSoup

def generate_downlown_link():
    file_path = r'D:\Program Files\pycharm\graph2vec-master\download_APK\360'

    querystring = {"page": 1}
    url = "http://zhushou.360.cn/list/index/cid/1"
    for i in range(3, 110):
        querystring["page"] = i
        html_doc = requests.request("GET", url, params=querystring)
        soup = BeautifulSoup(html_doc.content, "lxml")
        a_list = soup.select("#iconList > li > a.dbtn")
        for a in a_list:
            download_url = a.attrs["href"].split("&url=")[1]
            with open(file_path,"a+") as result:
                result.write(download_url + '\n')
            result.close()

def download_apk():
    download_link = r'D:\Program Files\pycharm\graph2vec-master\download_APK\360-100.txt'
    with open(download_link, 'r') as f:
        for link in f.readlines():
            file_name = link.split('/')[-1].split('\n')[0]
            print("G:\\gxt\\apk\\benign\\360\\"+file_name)
            if os.path.exists("G:\\gxt\\apk\\benign\\360\\"+file_name) == False:
                urllib.request.urlretrieve(link,"G:\\gxt\\apk\\benign\\360\\"+file_name)
                print("%s downloaded!\n" % file_name)
            else:
                print("----- "+file_name+" is exists")
                continue

def remove():
    file_path = r'D:\Program Files\pycharm\graph2vec-master\download_APK\360'
    with open(file_path,'r') as f:
        result=set(f.readlines())
    print("---- ",len(result))
    for link in result:
        file_name = link.split('/')[-1].split('\n')[0]
        print("G:\\gxt\\apk\\benign\\360\\" + file_name)
        if os.path.exists("G:\\gxt\\apk\\benign\\360\\" + file_name) == False:
            urllib.request.urlretrieve(link, "G:\\gxt\\apk\\benign\\360\\" + file_name)
            print("%s downloaded!\n" % file_name)
        else:
            print("----- " + file_name + " is exists")
            continue

# generate_downlown_link()
# download_apk()
remove()
