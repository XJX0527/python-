# -*- codeing = utf-8 -*-
# @Time:2021/6/28 15:40
# @Author:A20190277
# @File:data_read.py
# @Software:PyCharm

''''''
'''数据读入'''
import numpy as np
import pandas as pd
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv")
#特殊情况
#1.数据集无列名
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv",header=None)
#2.若想指定列名
columns=train.columns
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv",header=columns)
#3.指定数据类型
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv",dtype={'Age':np.float64})
train.dtypes  #查看各列数据类型
#4.只读取部分列的数据
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv",index_col=0,usecols=['Age','Cabin'])
#index_col=0：将第0列作为index
'''txt文件'''
#5.分隔符的使用
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.txt",sep=' ')
#6.读取时跳过前几行
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.txt",sep=' ',skiprows=[0,1]) #跳过第0行和第1行数据
#7.读取一部分数据
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.txt",sep=' ',skiprows=5,nrows=5)  #跳过前5行数据，后读取5行数据
'''其它格式的文件'''
#8.excel文件
train=pd.read_excel(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.xlsx",sheet_name='表格一')  #指定读取excel中的‘表格一’中的数据
#9.json文件
train=pd.read_json(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.josn")
#10.数据库数据和HDF5格式的数据
import sqlite3
connect=sqlite3.connect(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.sqilte") #将数据导入到connect中
train.to_sql('train_data',connect,if_exists='replace')  #将数据写入数据库中的train_data表中，若存在则替换
connect.commit()  #使得上述代码生效
connect.close()  #关闭数据库的链接
train_data=pd.read_sql('select * from trainn_data',connect)  #读取数据
print(train_data.head())
#11.读取网页数据
train=pd.read_html(f"https://movie.douban.com/top250?start=")

'''与read_csv相对的是to_csv（写入数据），
    与read_excel相对的是to_excel（import xlwt  #写入数据时要用到该库）
    用法与其基本一致，不加以与例'''

from pandas import ExcelWriter
with ExcelWriter(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.xls") as writer:
    train.to_excel(writer,sheet_name='test1')
    train.to_excel(writer,sheet_name='teat2')











