# -*- codeing = utf-8 -*-
# @Time:2021/6/29 7:47
# @Author:A20190277
# @File:e-commerce_analytics.py
# @Software:PyCharm
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
'''
#'StockCode'--证券代码
#'Description'---所购物品描述
#'Quantity'---数量，'UnitPrice'---单价
#'InvoiceDate'---发票日期，'InvoiceNo'---发票号码 
#'CustomerID','Country'
'''

df=pd.read_csv(r'C:\Users\18356\pythoxjx\Online_Retail.csv')
#,parse_dates=['InvoiceDate']
print(df.head(),df.columns)
print(df.info(),df.isnull().sum(),df.isnull().mean())
print(df.describe())
print('ID缺失值最多，占比也多，所有不能简单删除处理，Description缺失值较少，占比0.0026，所以可进行简单删除处理')
df['CustomerID']=df['CustomerID'].fillna(method='ffill')   #根据csv文件简单推测缺失值可能和上下值中的某一个相同，这里填充值选取上值
print(df.isnull().mean())
df=df.dropna()   #删除缺失值
print(df.isnull().mean())
print('缺失值处理完毕，CustomerID数据类型应该为int，InvoiceDate为日期数据，Description将其转化为小写字符串，修改其数据类型')
df['CustomerID']=df['CustomerID'].astype('int64')  #注意要先处理完缺失值，才能进行类型转换
#df['InvoiceDate']=datetime.strptime(df['InvoiceDate'],'%Y/%m/%d%H:%M')  #该方法一直报错，所以在导入数据时就对该数据类型进行修改即可
df['Description']=df['Description'].str.lower()
print(df.info())
print(df.describe(),'由于Quantity最大最小值相同，所以判断该客户错误购买后退货，所以删除该异常值')
print(df[df['Quantity']==80995])
print(df[df['Quantity']==-80995])
print('发现是同一客户ID，所以判断正确，删除这两行数据')
df=df.drop([540421,540422],axis=0)
print(df.describe())
# plt.boxplot(df['Quantity'])
# plt.show()
print(df[df['Quantity']==74215])
print(df[df['Quantity']==-74215])
df=df.drop([61619,61624],axis=0)
print(df.describe())
print(df[df['Quantity']==-9600])
print(df[df['Quantity']==12540])   #购买数量的缺失值处理完毕！
#异常值暂时处理完毕
'''添加新列'''
df['sum']=df['Quantity']*df['UnitPrice']
print(df.head(),df.columns)
'''将日期细分'''
def getYear(date):
    str1=date.split('/')[0]
    str1=str1.strip()
    year=int(str1)
    return year
df['year']=df['InvoiceDate'].map(getYear)
def getMonth(date):
    str1=date.split('/')[1]
    str1 = str1.strip()
    month = int(str1)
    return month
df['month']=df['InvoiceDate'].map(getMonth)
def getDay(date):
    str1=date.split('/')[2]
    str2=str1.split(' ')[0]
    str2 = str2.strip()
    day = int(str2)
    return day
df['day']=df['InvoiceDate'].map(getDay)
def getHour(date):
    str1=date.split('/')[2]
    str2 = str1.split(' ')[1]
    str3=str2.split(':')[0]
    str3 = str3.strip()
    hour = int(str3)
    return hour
df['hour']=df['InvoiceDate'].map(getHour)
df['YearMonth']=df['year']*100+df['month']
print(df['YearMonth'].head())
print(df.info())
print('=***********************************************************=')
'''EDA：本次探索数据为：订单量最大的10个客户是谁，消费最多的10位客户是谁，每个客户的消费金额是多少，每个客户的订单数是多少，消费者最喜欢在哪个时间段消费'''

print('---------------------订单量最大的10个客户是谁：可视化数据-------------------------')
a=df.groupby(by=['CustomerID','Country'],as_index=False)['InvoiceNo'].count()  #得到每个国家的客户的订单数目
print(a.head(10))
b=a.sort_values(by='InvoiceNo',ascending=False)
print(b.head(10))  #订单量最大的10个客户的ID和国家已知，猜想订单量最大的国家是United Kingdom
'''
#验证猜想：数据可视化
a_country=df.groupby(by=['Country'],as_index=False)['InvoiceNo'].count()  #得到每个国家的客户的订单数目
b_country=a_country.sort_values(by='InvoiceNo',ascending=False)
print(b_country.head(5))
print(b_country.head(10))
x=b_country['InvoiceNo']
y=b_country['Country']
plt.barh(y,x,color='r')
plt.xlabel('number')
plt.ylabel('country')
plt.title('number---country')
plt.show()

#去掉 United Kingdom 再次可视化
print(b_country[b_country['Country']=='United Kingdom'])
d_country=b_country.drop([36],axis=0)
x=d_country['InvoiceNo']
y=d_country['Country']
plt.barh(y,x,color='r')
plt.xlabel('number')
plt.ylabel('country')
plt.title('number---country')
plt.show()
'''

print('---------------------消费金额最大的10个客户是谁：可视化数据-------------------------')
money_order=df.groupby(by=['CustomerID','Country'],as_index=False)['sum'].sum()
print(money_order.head(10))
money=money_order.sort_values(by='sum',ascending=False)
print(money.head(10))  #发现订单数量和消费金额并无紧密联系，但是消费金额最多的应该还为United Kingdom
money_order=df.groupby(by=['Country'],as_index=False)['sum'].sum()
money=money_order.sort_values(by='sum',ascending=False)
print(money.head(10))
'''
#验证猜想：数据可视化
x=money['sum']
y=money['Country']
plt.barh(y,x,color='r')
plt.xlabel('money')
plt.ylabel('country')
plt.title('money---country')
plt.show()

#去掉 United Kingdom 再次可视化
print(money[money['Country']=='United Kingdom'])
money=money.drop([36],axis=0)
x=money ['sum']
y=money['Country']
plt.barh(y,x,color='r')
plt.xlabel('sum')
plt.ylabel('country')
plt.title('money---country')
plt.show()
'''

print('-------------------消费者喜欢的购物时间，呜呜呜呜呜呜呜呜不会可视化做这个图--------------------')
#由于该数据来自于英国，所以查看圣诞节期间知否订单激增
#df.to_csv(r'C:\Users\18356\pythoxjx\xjx.csv',index=False)
ax_month=df.groupby(by=['YearMonth'],as_index=False)['Quantity'].sum()
b_month=ax_month.sort_values(by='Quantity',ascending=False)
print(b_month)    #可以看出11月份的订单量最多
ax_hour=df.groupby(by=['hour'],as_index=False)['Quantity'].sum()
b_hour=ax_hour.sort_values(by='Quantity',ascending=False)
print(b_hour)  #人们最喜欢在正午消费，所以建议在中午时刻增加客服人员，使其购物体验良好

#https://blog.csdn.net/weixin_48615832/article/details/108028198：可视化讲解网址CSDN

print('---------------------------------------------')
print('---------------------------------------------')
print('-----------------------客户留存分析---------------------------')
'''
以时间为维度，对客户留存进行分析，这里选取月为度量维度
'''
n_month={
        201012:1,
        201101:2,
        201102:3,
        201103:4,
        201104:5,
        201105:6,
        201106:7,
        201107:8,
        201108:9,
        201109:10,
        201110:11,
        201111:12,
        201112:13
}
df['month']=df['YearMonth'].map(n_month)
print(df['month'].unique())

group=df.groupby(by='CustomerID',as_index=False)['month']
df['month_first']=group.transform('min')
print(df.columns)
print(df.tail())
df['month_period']=df['month']-df['month_first']+1
print(df.tail(),df.head())
#df.to_csv(r'C:\Users\18356\pythoxjx\new_xjx.csv',index=False)

#将数据按照要求可视化即可


