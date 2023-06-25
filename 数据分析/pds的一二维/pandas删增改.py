import numpy as np
import pandas as pd


# pf = pd.DataFrame(np.arange(1,17).reshape(4,4),index=["a","a","d","d"],columns=["A","B","C","D"])
#
# #     A   B   C   D
# # a   1   2   3   4
# # b   5   6   7   8
# # c   9  10  11  12
# # d  13  14  15  16
#
# pf["A"]=["wen","li","fen","good"]
# pf.loc["a"]=["w","w","e","n"]
# pf.loc["b","C"]="fenfen"
# pf.iloc[1,3]="fenfen"
#
# rename1 = pf.rename(index={"a":"yes"},inplace=True)  # 改索引名
# # print(rename1)
#
# # print("*"*200)
# # 增加
# pf["f"] = 17
# # print(pf)
# #    A   B   C   D   f
# # a   1   2   3   4  17
# # b   5   6   7   8  17
# # c   9  10  11  12  17
# # d  13  14  15  16  17
# s1 = pd.Series(np.arange(4),index=["A","B","C","D"])
# p = pf.append(s1,ignore_index=True)  # 忽略索引值
# # print(p)
# #       A     B     C     D     f
# # 0   1.0   2.0   3.0   4.0  17.0
# # 1   5.0   6.0   7.0   8.0  17.0
# # 2   9.0  10.0  11.0  12.0  17.0
# # 3  13.0  14.0  15.0  16.0  17.0
# # 4   0.0   1.0   2.0   3.0   NaN
#
# dict = {"A":"son","B":"father","C":"mother"}
# add = p.append(dict,ignore_index=True)
# # print(add)
# #     A       B       C     D     f
# # 0    1       2       3   4.0  17.0
# # 1    5       6       7   8.0  17.0
# # 2    9      10      11  12.0  17.0
# # 3   13      14      15  16.0  17.0
# # 4    0       1       2   3.0   NaN
# # 5  son  father  mother   NaN   NaN


# 删除
pf = pd.DataFrame(np.arange(1,17).reshape(4,4),index=["a","d","a","d"],columns=[["a","a","b","b"],["A","B","A","B"]])
pf.swaplevel(axis=1)
print(pf)
pf.sum(level=0)
print(pf)

#     A   B   C   D
# a   1   2   3   4
# b   5   6   7   8
# c   9  10  11  12
# d  13  14  15  16
# sc1 = pf.drop("A",axis=1)
# print(sc1)
# sc2 = pf.drop(2)
# print(sc2)
# del pf["A"]
# print(pf)
# del pf[1]
# print(pf)
# arr1 = pd.Series(np.arange(6))
# arr2 = arr1.drop(2)
# print(arr2)

# pf["B"]=["20","60","100","140"]
# print(pf)
# pf.loc[0]=["20","60","100","140"]
# pf.iloc[1,1]="dog"
# print(pf)

# pf.rename(index={1:"one"},columns={"C":"c"},inplace=True)
# print(pf)
