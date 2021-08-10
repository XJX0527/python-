# -*- codeing = utf-8 -*-
# @Time:2021/6/28 10:44
# @Author:A20190277
# @File:data reorganization.py
# @Software:PyCharm

''''''
'''整理数据'''
import pandas as pd
import numpy as np
train=pd.read_csv(r'C:\Users\18356\pythoxjx\pew-raw.csv')
print(train)
#id_vars：定义新列名字，var_name：将原来的列进行重新命名
#id_vars：保持原样的列

#var_name：转换后变量的列名
#value_name：数值变量的列名

#value_vars：需要被转换为变量值的数据列
new_train=pd.melt(train,id_vars=['religion'],var_name='income',value_name='freg')  #melt()融合函数
new_train=new_train.sort_values('religion')  #排序
print(new_train)

#用数据堆叠进行处理
new_train=train.set_index('religion')   #set_index：将该列设置为行索引
new_train=new_train.stack()    #stack()：将所有的列进行堆叠，将其作为二级索引
print(new_train.head())
new_train.index=new_train.index.rename('income',level=1) #将二级索引命名
new_train.name='freg'   #数值变量的命名
new_train=new_train.reset_index()  #重置列名
print(new_train.head())
print('=**************************************************************************=')

#进一步理解melt函数
df=pd.read_csv(r'C:\Users\18356\pythoxjx\billboard.csv',encoding='mac_latin2')
print(df.head())
print(df.columns)
#id_vars：保持原样的列
id_vars=['year','artist.inverted','track', 'time', 'genre', 'date.entered','date.peaked']
#var_name：转换后变量的列名
df=pd.melt(df,id_vars=id_vars,var_name='weeks',value_name='rank')  #value_name：数值变量的列名，value_vars：需要被转换为变量值的数据列
print(df.head())
#但是weeks列对应是值应该是数值
def getweeks(week):
    str1=week.split('.')[0]
    str2=str1.split('x')[1]
    str3=str2.split('s')[0]
    str4=str3.strip()
    return str4
weeksdf=pd.DataFrame()
weeksdf['week']=df['weeks'].map(getweeks)
df=pd.concat([df,weeksdf],axis=1)
df.drop('weeks',axis=1,inplace=True)
print(df.head())
#另一种方法：正则表达式法处理weeks
df['week']=df['weeks'].str.extract('(\d+)',expand=False).astype(int)
print(df.head())
print('=**************************************************************************=')

'''多个变量储存在一列中'''
df=pd.read_csv(r'C:\Users\18356\pythoxjx\tb-raw.csv')
print(df.head())  #将性别和年龄都放在了列命中
df=pd.melt(df,id_vars=['country','year'],value_name='cases',var_name='sex_and_age')
print(df.head())
#利用正则表达式提取性别，年龄上下限
tmp_df=df['sex_and_age'].str.extract("(\D)(\d+)(\d{2})",expand=False)
tmp_df.columns=['sex','age_lower','age_upper']
tmp_df['age']=tmp_df['age_lower']+'-'+tmp_df['age_upper']
df=pd.concat([df,tmp_df],axis=1)
#清理不需要的行和列
df=df.drop(['sex_and_age','age_lower','age_upper'],axis=1)
df=df.dropna()
df=df.sort_values(by=['country','year','sex','age'],ascending=True)
print(df.head())
print('=**************************************************************************=')

'''变量既在列中储存又在行中储存'''
import datetime
df=pd.read_csv(r'C:\Users\18356\pythoxjx\weather-raw.csv')
print(df.head())
df=pd.melt(df,id_vars=['id','year','month','element'],var_name='day_raw')
print(df.head())
def getDay(day):
    str1=day.split('d')[1]
    str2=str1.strip()
    return str2
dayDf=pd.DataFrame()
dayDf['day']=df['day_raw'].map(getDay)
df=pd.concat([df,dayDf],axis=1)
#df.drop('day_raw',axis=1,inplace=True)
print(df.head())
print('----------------------')
#合并year  month day为date
df['id']='MX17004'
df[['year','month','day']]=df[['year','month','day']].apply(lambda x:pd.to_numeric(x,errors='ignore'))
print(df.head())
print('--------------')
def create_date_from_year_day(row):  #建立新的date列
    return datetime.datetime(year=row['year'],month=int(row['month']),day=row['day'])
df['date']=df.apply(lambda row:create_date_from_year_day(row),axis=1)   #将这几列转换为数字
df=df.drop(['year','month','day','day_raw'],axis=1)
print(df.head())
#拆分tmin,tmax列
df=df.dropna()
df=df.pivot_table(index=['id','date'],columns='element',values='value')
print(df)
df.reset_index(drop=False,inplace=True)
print(df)
print('=**************************************************************************=')

