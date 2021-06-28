# -*- codeing = utf-8 -*-
# @Time:2021/6/28 16:25
# @Author:A20190277
# @File:data_merge.py
# @Software:PyCharm
''''''
import pandas as pd
import numpy as np
import datetime
'''数据合并'''
customers={'CustomerID':[10,11],'Name':['Tom','Alice'],'Address':['USA','China']}
customers=pd.DataFrame(customers)
print(customers,type(customers))
orders={'CustomerID':[10,11,10],'OrderDate':[datetime.date(2016,12,1),datetime.date(2016,12,1),datetime.date(2016,12,2)]}
orders=pd.DataFrame(orders)
print(orders)
#合并数据集
new_data=customers.merge(orders)
print(new_data)

left_data={'key1':['a','b','c'],'key2':['x','y','z'],'lvall':[0,1,2]}
right_data={'key1':['a','b','c'],'key2':['x','a','z'],'lvall':[6,7,8]}
left=pd.DataFrame(left_data,index=[0,1,2])
right=pd.DataFrame(right_data,index=[1,2,3])
print(left)
print(right)
print('----')
print(left.merge(right))  #key1与key2都相同，才能合并
print('----')
m=left.merge(right,on='key1')  #指定on=key1为合并列
print(m)
print('------')
w=pd.merge(left,right,left_index=True,right_index=True)  #按索引进行合并
print(w)
print('=*****************************************=')
'''merge()函数的进一步讲解'''
'''
inner：内连接
outer：外连接（并集）
left：左连接
right：外连接
'''
a=left.merge(right,how='outer')
print(a)
b=left.merge(right,how='inner')
print(b)
c=left.merge(right,how='left')  #保留left中的数据，用right中的数据进行填充
print(c)
d=left.merge(right,how='right')
print(d)
print('---------')
'''补充讲解：join，concat'''
# a=left.join(right)
# #左边数据集的列加上后缀_left，右边数据集加上后缀_right
# print(a)
# # a=left.join(right,lusffix='_left',rsuffix='_right')  #左边数据集的列加上后缀_left，右边数据集加上后缀_right
# # print(a)
# # b=left.join(right,lsuffix='_left',reuffix='_right',how='outer')
# # print(b)
# # c=left.join(right,lsuffix='_left',rsuffix='_right',how='inner')
# # print(c)
#full=pd.concat([full,titleDf],axis=1)


