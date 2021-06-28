# -*- codeing = utf-8 -*-
# @Time:2021/6/27 20:53
# @Author:A20190277
# @File:pandas_data analytics.py
# @Software:PyCharm

#元数据
import numpy as np
import pandas as pd
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv")
print(train.head())
print(train.shape)  #行和列
print(train.size)  #行*列
print(train.ndim)  #数据维度

#数据类型转换，若有缺失值是要先把缺失值补齐（fillna()）
#train['Cabin']=train['Cabin'].astype('int')  #转为int类型

#缺失值数据处理
a=train.isnull().sum()  #缺失值个数
print(a)
b=train.duplicated().sum() #查看重复数据
print(b)
c=train[train.duplicated()].head() #查看具体的重复值
print(c)

train.isnull() #缺失值为真
train.notnull() #缺失值为假
train['Cabin'].dropna()  #删除该列的缺失值
train.dropna()           #该行存在缺失值则删除
train.dropna(how='all')  #整行数据都缺失才删除
train.drop(axis='all')   #整列数据都缺失才删除
train.drop(thresh=3)     #一行中存在多余3个缺失值的进行删除

#train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv",na_values=[0])
#na_values=[0]：表示如果数据中有数值为0，则该值代表缺失值

'''numpy,pandas对缺失值数据处理的区别'''
#加法运算
import pandas as pd
import numpy as np
#numpy处理缺失值，只要遇到缺失值就返回NAN，pandas则是跳过缺失值继续处理数据
a=np.array([np.nan,1,2,np.nan,3])
print(a,a.mean())
s=pd.Series(a)
print(s,s.mean())

#填充缺失值.fillna
train['Age']=train['Age'].fillna(0,limit=3)  #AGE中的缺失值填充3个就不继续填充了
train['Age']=train['Age'].fillna(train['Age'].mean())   #用平均值填充
train['Age']=train['Age'].fillna(method='ffill')  #用该缺失值的前一个数据进行填充
train['Age']=train['Age'].fillna(method='bfill')  #用该缺失值的后一个数据进行填充
#用编写的值进行填充
fill_values=pd.Series([1,2],index=['b','c'])
train['Age']=train['Age'].fillna(fill_values)
#用插值进行填充.interpolate()
s=pd.Series([1,2,np.nan,5,np.nan,9])
s.interpolate()
#当索引为时间时，考虑时间间隔的问题进行插值method="time"
import datetime
ts=pd.Series([1,np.nan,2],index=[datetime.datetime(2016,1,1),datetime.datetime(2016,2,1),datetime.datetime(2016,4,1)])
print(ts)
ts.interpolate()
ts.interpolate(method="time")
#考虑索引的插值method='values'
pd.Series([0,np.nan,20],index=[0,1,10])
print(s.interpolate())
s.interpolate(method='values')

'''处理重复值'''
print(train.duplicated())  #返回bool值
train.drop_duplicates()  #删除重复值，只保留一个
train.duplicated(['Age','Cabin'])  #指定列，查看是否存在重复值

'''处理异常值：1.根据实际，2.根据数据字典给出的范围，3.数据标准差'''
#以下为数据标准差的例子
print(train['Age'].loc[33])
m=train[np.abs(train['Age']-train['Age'].mean())<=(2*train['Age'].std())]  #构造的数据标准差Dataframe
print(m['Age'])
#筛选出在标准差之外的数据
mask=np.abs(train['Age']-train['Age'].mean())>=(2*train['Age'].std())
print(train[mask]['Age'])
#将这些数值用平均值代替
train[mask]=train['Age'].mean()
print(train[mask]['Age'])
print(train['Age'].loc[33])

'''描述性统计：前提是缺失值、异常值、重复数据处理完毕'''
l=train.describe(include=[np.number]).T  #选择数据框中的数值类型列，T的意思是行列变换
#describe()：数据计数，均值，最大最小值，标准差，第1，2，3，分位数
print(l)
k=train.describe(include=[np.object]).T  #对于非数值类型，describe输出的是：数据计数、不同值个数、出现频率等
print(k)
w=train.nunique() #输出不同值个数的计数
print(w)

#查看最大最小值的前50个数
print((train.nlargest(50,'Age').head())['Age'])
print((train.nsmallest(50,'Age').head())['Age'])
#对数据排序
train.sort_values('Age',ascending=False).head()  #False：降序
train.sort_values('Age','Cabin',ascending=False).head()   #指定多列排序，先根据Age后根据Cabin排序