import pandas as pd
import numpy as np

arr1 = pd.Series(np.array([4,5,7,3]),index=['a','b','c','d'])
print(arr1)
arr1[0]=12
print(arr1)
dirt={
    "李白":"诗仙",
    "杜甫":"诗圣",
    "李贺":"诗魔"
}
arr2 = pd.Series(dirt)
print(arr2)

pf = pd.DataFrame(np.arange(16).reshape(4,4),index=["a","b","c","d"],columns=["A","B","C","D"])
print(pf)
#     A   B   C   D
# a   1   2   3   4
# b   5   6   7   8
# c   9  10  11  12
# d  13  14  15  16
dirt1={
    "李白":["诗仙"],
    "杜甫":["诗圣"],
    "李贺":["诗魔"]
}
df = pd.DataFrame(dirt1)
print(df)
#    李白  杜甫  李贺
# 0  诗仙  诗圣  诗魔

