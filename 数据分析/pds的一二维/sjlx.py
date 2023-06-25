import pandas as pd
import numpy as np

view = pd.read_csv("运动员信息表1.csv",encoding="gbk")
print(view)
df = pd.DataFrame(view)

# print(view.dropna(subset=["项目"]),"\n",view.isna().sum())
# print(pd.DataFrame.fillna(view,value=df["年龄（岁）"].mean()))
print("=0"*30)
print("************************************************")
tz = df.iloc[:,5]
tz1=tz[tz<50]

tz2 = tz[tz>150].dropna(how="all")
print(tz2)
print(df)
df.drop(df[df["体重(kg)"]>150].index,inplace=True)
# ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
print("************************************************")
# print(df["项目"].str.cat(others=df["性别"],sep="_"))