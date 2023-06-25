import numpy as np
import pandas as pd

pf1 = pd.DataFrame(np.arange(16).reshape(4,4),index=["a","b","c","d"],columns=["A","B","C","D"])
#     A   B   C   D
# a   1   2   3   4
# b   5   6   7   8
# c   9  10  11  12
# d  13  14  15  16
print(pf1[:1])  # 取行
print(pf1["A"])  # 取列 只能用标签
print(pf1[["A","C","D"]])  # 取多列
print(pf1["A"][1])  # 取单个数
print(pf1.loc["a":"c","A":"C"])  # 连续
print(pf1.loc[["a","d"],["A"]])  # 不连续
print(pf1.iloc[:3,:3])  # 连续
print(pf1.iloc[:3,[1,3]])  # 列不连续
# print(pf1.ix[:3,:3])
