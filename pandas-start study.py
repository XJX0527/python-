# -*- codeing = utf-8 -*-
# @Time:2021/6/26 21:35
# @Author:A20190277
# @File:pandas-start study.py
# @Software:PyCharm

import pandas as pd
#pandas中有两种基础类型数据：series---由一组数据以及一组与之相关的索引组成，dataframe---表格型数据结构
'''dataframe基本要素：索引、列、数据'''
train=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv")
print(type(train))
print(train.dtypes)     #dataframe中的数据中的每一列必须是同一种数据类型
print(train.head())
print('================================================================================')
index=train.index       #索引，0~891，step=1，数据类型：RangeIndex
columns=train.columns   #列名，数据类型：Index
data=train.values       #数据内容，数据类型：ndarray
print(index,type(index))
print(columns,type(columns))
print(data,type(data))
print('================================================================================')
print(issubclass(pd.RangeIndex,pd.Index))  #说明RangeIndex与Index是同一数据类型
print(index.values)    #显示数据内容
print(columns.values)  #显示数据内容
print('=*******************************************************************************=')

'''series：dataframe的每一列'''
AGE=train['Age']
print(AGE,type(AGE))
#也可利用此方法访问数据，但是不建议此法，print(train.Age)
#AGEE=train['Age']+1，可对数据进行算数运算，布尔运算等等
print('=*******************************************************************************=')

'''链式方法'''
AGE=train['Age'].head()
print(AGE)
Embar=train['Embarked'].value_counts()  #统计频数
print(Embar)
Embar=train['Embarked'].isnull()       #判断该行数据是否缺失
print(Embar)
Embar=train['Embarked'].isnull().sum() #查看缺失值数
print(Embar)
Embar=train['Embarked'].isnull().mean() #查看缺失值占比
print(Embar)
Embar=train['Embarked'].fillna('W').isnull().mean() #利用’W‘对缺失值进行填充，后查看缺失值占比
print(Embar)
print('=*******************************************************************************=')

Embar=train['Cabin'].fillna('W').head()
print(Embar)
print(train['Cabin'].head())
#发现对原数据中的数据并无影响
#若要对原数据修改则采取以下方法
train['Cabin'].fillna('W',inplace=True)
print(train['Cabin'].head())
print('=*******************************************************************************=')

'''修改索引和列'''
#默认索引值是0，1，2.....
#若想利用数据中的某一列作为索引列，则
tra=pd.read_csv(r"C:\Users\18356\Desktop\Kaggle\Titanic-Machine Learning from Disaster\titanic\train.csv",index_col='Age')
print(tra.head())
#或者---print(train.set_index('Age').head())  #train.set_index('Age')是一个新对象
print(tra.reset_index())  #恢复默认索引列
#修改列名
new_colums={'Age':'x1','PassengerId':x3......}
train.rename(columns=new_colums,inplace=True)
print(train.index())
#添加列
train['MMM']=train['Age']+1  #默认加到最后一列
print(train.head())
#删除列
train.drop('MMM',axis='columns',inplace=True)
print(train.head())
#或者
del train['WWW']

#列的选取可以根据名称直接选取
#也可以选取包含某个字符串的数据
train.filter(like='A')
train.filter(regex='A')




