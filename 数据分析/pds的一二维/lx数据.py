import re

import pandas as pd
import numpy as np

# view = pd.read_csv("运动员信息表.csv",encoding="GBk")
# view["省份"]=view["省份"].str.strip()
# print(view.groupby(by="省份").count()["姓名"])
# nn = view.groupby(by=["省份","性别"]).count()
# print(nn["姓名"])
# # print(nn)
# print(view.groupby(by=["性别"])["年龄（岁）"].max())

view = pd.read_csv("运动员信息表.csv",encoding="GBK")
print(view)
lxy1 = view.groupby(by=["项目","性别"]).agg({"身高(cm)":np.mean,"体重(kg)":np.mean,"年龄（岁）":np.mean})
print(lxy1.loc["篮球",:])


def my_range(arr):
    return arr.max() - arr.min()


lxy2 = view.groupby(by=["性别"]).agg({"身高(cm)":my_range,"体重(kg)":my_range,"年龄（岁）":my_range})
print(lxy2)
print("*"*60)

result1 = pd.pivot_table(view,values=["年龄（岁）","体重(kg)"],index=["项目"])
print(result1.head(10))
result2 = pd.pivot_table(view,values=["年龄（岁）","体重(kg)"],index=["项目"],aggfunc=[min,max])
print(result2)

print("*"*80)
result3 = pd.crosstab(view["省份"],view["性别"])
print(result3.head())


