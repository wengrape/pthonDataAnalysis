import numpy as np
import pandas as pd

dirt1 = {
    "city":["上海","天津","厦门"],
    "name":["小A","小B","小白"],
    "sex":["12","34","25"]
}

arr1 = pd.DataFrame(dirt1)
print(arr1)
#  city name sex
# 0   上海   小A  12
# 1   天津   小B  34
# 2   厦门   小白  25
p = arr1.insert(3,"age",[99,99,99])  # 插入的位置  列名  列值
print(arr1)
#  city name sex  age
# 0   上海   小A  12   99
# 1   天津   小B  34   99
# 2   厦门   小白  25   99
arr1["work"] = ["程序员","CEO","主持人"]
print(arr1)
#   city name sex  age work
# 0   上海   小A  12   99  程序员
# 1   天津   小B  34   99  CEO
# 2   厦门   小白  25   99  主持人
