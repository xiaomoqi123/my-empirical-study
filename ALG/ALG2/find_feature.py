import numpy as np



# X = np.loadtxt("./result/2_gram.csv",skiprows=1, delimiter=',', dtype=int)
#
# print(X[0, :])

import xlrd                           #xlrd是excel文件读取库 只读写
import pandas as pd


# data = xlrd.open_workbook('./result/2_gram.csv')   #打开excel文件
# table = data.sheets()[0]              #打开第一张表格
# nrows = table.nrows
#
# for i in range(nrows):
#     name_.append(table.row_values(i)[0])
#     data_.append(table.row_values(i)[0:48])
#
# dict_data = dict(zip(name_,data_))
# data  = pd.DataFrame(dict_data,index=name_)
# print (data_.T)

csv_data = pd.read_csv('./result/5_gram.csv')  # 读取训练数据
# print(type(csv_data))
# print(csv_data.shape)
col_sum = csv_data[7618:15234].sum(axis = 0)
# print(type(col_sum))
# print("------")
print(col_sum.sort_values(ascending=False)[0:11])