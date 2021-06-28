# -*- codeing = utf-8 -*-
# @Time:2021/6/28 19:05
# @Author:A20190277
# @File:data_matplotlib.py
# @Software:PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# plt.plot([1,2,3,4,8])
# plt.show()
'''
eg.
r*--：r红色，*星号，--虚线
ks.：k黑色，s方块.点
bD-.：b蓝色，D钻石点，-.点划线
print(help(plt.plot))
'''
# plt.plot([1,2,4,5],[3,5,6,8],'ro')
# plt.show()

# plt.plot([1,2,4,5],[3,5,6,8],'g*',label='Green Star')
# plt.plot([2,5,7,8],[0,3,5,6,],'bD',label='Blue Diamond')
# plt.title('SSSS')  #注意中英文，应该是只能英文
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend(loc='best')  #画布的大小和位置best
# plt.show()

#中文
# plt.figure(figsize=(12,9))  #画布的长宽比
# plt.xlim(0,12)
# plt.ylim(0,12)
plt.rcParams['font.sans-serif']=['SimHei']  #显示中文字体，SmiHei为字体样式
plt.rcParams['axes.unicode_minus']=False    #坐标轴有负号时可以显示负号
plt.plot([1,2,4,5],[3,5,6,8],'g*',label='绿星星')
plt.plot([2,5,7,8],[0,3,5,6,],'bD',label='蓝钻石')
plt.title('散点图')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')  #画布的大小和位置best
plt.show()





