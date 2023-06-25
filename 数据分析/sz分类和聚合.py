import numpy as np
import pandas as pd

df = pd.DataFrame({
    "key1":["A","B","C","B","A"],
    "key2":["one","two","one","two","one"],
    "key3":[2,3,4,5,6],
    "key4":[7,6,5,4,3]
})

# print(df)
# print("*"*90)
# # 按单个列来分组
# groupby_obj1=df.groupby(by="key1")
# for i in groupby_obj1:
#     print(i)
# print("8"*90)
# groupby_obj2 = df.groupby(by=["key1","key2"])
# print(groupby_obj2)
# for i in groupby_obj2:
#     print(i)
