import pandas as pd
import numpy as np
import re

ds1 = pd.Series(["a","b",np.nan],index=["A","B","C"])
df1 = pd.DataFrame([["d","e"],["e","f"],["j","h"]],index=["A","B","C"])
lj1 = ds1.str.cat(others=df1,sep="-",na_rep="空")
print(lj1)
print(lj1.str.split(pat="-",n=2,expand=True))
print(lj1.str.get(1))
print("*"*40)
# ds2 = pd.Series(np.arange(6))
# df2 = pd.DataFrame(np.arange(12).reshape(2,6))
# print(ds2.str.cat(others=df2))  # AttributeError: Can only use .str accessor with string values!

str1 = "密码:3333,手机号:123456,用户号：666666,用户密码:aaaaaa";
patt1 = ":.*,"
patt2 = ":(.*?),"
print(re.search(patt1,str1))
print("gounps:",re.search(patt1,str1).group())
print(re.findall(patt2,str1))
print("8"*50)

patt3 = ":.*,"
pattern_str = re.compile(patt3,flags=re.I)
print(pattern_str.match(str1))


