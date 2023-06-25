import pandas as pd
import numpy as np

# Series 索引相同相加,不同为nan (为并集)

arr1 = pd.Series(np.arange(4),index=["a","b","a","c"])
arr2 = pd.Series(np.arange(2,6), index=["a","b","f","c"])
arr3 = arr2 + arr1
print(arr3)

# DataFrame rows,columns相同相加,不同为nan (为并集)
arr4 = pd.DataFrame(np.arange(12).reshape(3,4),index=["a","b","c"],columns=["A","B","C","D"])
arr5 = pd.DataFrame(np.arange(12).reshape(3,4),index=["a","b","e"],columns=["A","B","C","D"])
arr6 = arr4 + arr5
print(arr6)

# 函数应用
# apply() 到行或列
# apply(self, func, axis=0, raw=False, result_type=None, args=(), **kwds)
ln = lambda x: x.max()
print(arr4.apply(ln))
print(arr4)

# applymap() DataFrame 到每个数
ln1 = lambda x: "%.2f"%x
print(arr4.applymap(ln1))

# map() 到每个数 Series
print(arr1.map(ln1))


# Series 排列
print(arr3.sort_index())  # 索引排列
print(arr3.sort_values(ascending=False))  # 值排列

# DataFrame 排列
arr4.iloc[2,1]=34
arr4 = arr4.rename(index={"c":"a"})
print(arr4.sort_index(ascending=False))
# print(arr4.sort_values(by="A",axis=1))  # 查一下
print("*"*140)
print(arr1.unique())
# print(arr1.index.is_unique())  # 查一下
print(arr1.value_counts())

print("*"*190)
# 统计计算
# sum DataFrame
print(arr4.sum(axis=1))

# cumsum
print(arr4.cumsum())
print("*"*90)
print(arr4.describe())
