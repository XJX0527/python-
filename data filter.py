# -*- codeing = utf-8 -*-
# @Time:2021/6/27 11:38
# @Author:A20190277
# @File:data filter.py
# @Software:PyCharm

import pandas as pd
#.loc和.iloc筛选数据
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv")
country=train['Age']
#提取Age中的某一行
print(country.iloc[0],country.iloc[23],country.iloc[76])
print(country.iloc[[0,23,76]])
print(country.iloc[10:60:10])  #索引10~60，每隔10个选一个
s1=pd.Series([1,2,3,4],index=['A','B','C','D'])
s2=pd.Series([1,2,3,4],index=[4,1,3,2])
print(s1)
print(s1.iloc[[1,3]])
print(s2.iloc[[1,3]])

#但是对于索引有具体意义的用.loc来筛选数据
# train.loc['Tom']  #索引为Tom的行
# train.loc['Tom','Alice']
# train.loc['Tom':'Alice':10]

# #同时选取行列
# train.loc[rows,columns]
# train.iloc[rows,columns]

#查看数据位于第几行
print(train.columns.get_loc('Age'))

'''布尔选择'''
new_train=train['Age']>10  #大于10的为真（1），小于10的为假（0）
print(new_train.head())
new_train.mean()  #因为1，0的原因，这里的值为大于10的人占总数的百分比
new_train=train['Cabin'].isnull()
print(new_train.head())

#多条件筛选数据
c1=train['Age']>23
c2=train['Cabin']=='C'
c=c1&c2
train[c]


