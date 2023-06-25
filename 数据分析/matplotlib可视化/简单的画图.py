import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random



# df1 = pd.DataFrame(np.arange(1,101).reshape(10,10))
# print(df1)
# plt.plot(df1)
# plt.show()
# n_x = np.arange(1,10)
# n_y = np.arange(1,10)
# plt.plot(n_x,n_y)
# plt.show()


# view = plt.subplot(323)
# view.plot([2,3,1,5,3,7,20])
# plt.show()



# (fig, axes) = plt.subplots(2,2)
# ax1 = axes[0,0]
# ax1.plot([3,2,1,5,2,6,7,2,9])
# plt.show()

n = np.random.randint(4,19)
n_x = np.arange(4,19)
n_y1 = np.array([32,33,34,34,33,31,30,29,30,29,26,23,21,25,31])
n_y2 = np.array([19,19,20,22,22,21,22,16,18,18,17,14,15,16,16])
plt.figure(figsize=(12,8),facecolor="blue")
plt.plot(n_x,n_y1,label="最高温度")
plt.plot(n_x,n_y2,label="最低温度")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.xlabel("日期",labelpad=9)
xticks1 = np.arange(4,19,2)
data =["9月"+str(i)+"日" for i in xticks1]
plt.xticks(ticks=xticks1,labels=data)

# plt.xlim(left="9月4日",right="9月6日")

plt.ylabel("温度" ,labelpad=9)
y1 = np.arange(15,36,4)
summer1 = plt.yticks(ticks=y1,labels=[str(i)+"°" for i in y1])
plt.title("近段时间的温度变化")


# plt.xlim(1,4)
plt.legend()
plt.show()


plt.bar(n_x,n_y2,width=0.3)
plt.show()

# x = np.arange(10000,80000,10000)
x = np.array([10000,20000,30000,40000,50000,60000,70000])
y = np.array([1223,4531,7545,432,2344,2334,7544])
plt.bar(x,y,width=1000,bottom=1000,tick_label=[str(i) for i in range(1,8)])
plt.show()




