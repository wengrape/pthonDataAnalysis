import pandas as pd
import numpy as np

data_frame = pd.DataFrame(np.arange(36).reshape(6,6),columns=list('abcdef'))
data_frame["key"] = pd.Series(list('aaabbb'),name="key")
# print(data_frame)
data_groub = data_frame.groupby(by="key")
# print(data_groub)
group_sum = data_groub.agg(sum)
# print(group_sum)


def my_range(arr):
    return arr.max() - arr.min()


# print(data_groub.agg(my_range))

data_groub.agg([my_range,sum,np.mean])

reast = data_groub.agg({'a':np.mean,'b':sum,'c':my_range})
print(reast)
