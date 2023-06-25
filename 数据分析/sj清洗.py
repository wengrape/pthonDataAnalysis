import pandas as pd
import numpy as np
#
# arr1 = np.arange(16).reshape(4,4)
# arr2 = pd.DataFrame(arr1)
# print(arr2==np.nan)
# print(arr2)
# print("*"*40)
# arr2.iloc[2,3] = np.nan
# print(arr2)
# arr3 = pd.DataFrame.dropna(arr2)
# print("*"*40)
# print(arr3)
# print("*"*40)
# arr4 = pd.DataFrame.dropna(arr2,axis=1,how="any")
# print(arr4)
# arr5 = pd.fillna(value="2")
# print("="*40)
# print(arr5)

view = pd.read_csv("data/iris-data.csv")
print(view)
print(view.isnull().sum())
print(view.dropna())
print("="*50)
print(view.dropna(axis=1,how='any'))  #删除列
# print(view.fillna("wen",axis=1))
# print(view.duplicated(keep="first",subset=["sepal_length_cm"]))
# print(view.drop_duplicates(keep="first",subset=["sepal_length_cm","sepal_width_cm"]))
# print("[]"*40)
# print(view.dropna(axis=1,how='all'))  #删除列


arr1 = np.arange(16).reshape(4,4)
arr2 = np.arange(24).reshape(3,8)
arr3 = pd.DataFrame(arr1)
arr4 = pd.DataFrame(arr2)
he1 = pd.concat([arr3,arr4],axis=1,join="outer",keys=["a","b"],names=["fen1","fen2"])
print(he1)
he2 = pd.concat([arr3,arr4],axis=1,join='inner')
print(he2)
he3 = pd.concat([arr3,arr4],axis=0,join="outer")
print(he3)
he4 = pd.concat([arr3,arr4],axis=0,join='inner')
print(he4)