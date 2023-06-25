import numpy as np
import pandas as pd
import csv

arr1=np.arange(12).reshape(3,4)
print("arr1:",arr1)
arr2=pd.DataFrame(arr1,index=["a","b","c"],columns=["a","b","c","d"])
print("arr2:")
print(arr2)
print(arr2["c"])
print(arr2.loc["a"]["c"])
print(arr2.iloc[0:2,1:3])
print(arr2.iloc[:,:]>3)

hen=open('wen.csv','w',newline='')
hen1=csv.writer(hen)
print("hen1:",hen1)
hen1.writerow(("id","name","age","school"))
hen1.writerow(("1","温了和","18","a"))
hen1.writerow(("2","温了和","18","a"))

hen.close()
kj=pd.read_csv('wen.csv',names=["a","b","c","d"],index_col="a")
print(kj)

