import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# data = np.random.randint(1,100,50)
# data1 = np.random.randint(1,100,50)
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# plt.hist(data,bins=8,label="随机分布1")
# plt.plot(data1,label="随机分布2")
# plt.legend()
# plt.show()


# data2 = np.random.randint(20,50,10)
# label1 = ["A","B","C","D","E","F","G","H","I","J"]
# plt.figure(figsize=(6,6))
# plt.pie(data2,labels=label1,autopct="%.1f%%",radius=1,wedgeprops={"width":0.7})
# plt.title("饼形图")
# plt.show()

# pf = pd.DataFrame(np.random.randint(1,50,36).reshape(6,6),columns=["A","B","C","D","E","F"])
nr_x = np.random.randint(10,20,6)
nr_y = np.random.randint(10,20,6)
plt.plot(nr_x,nr_y,label="but",color="blue",linestyle=":")

plt.title("随机分配")
f_l = np.arange(4,19,2)
f = [str(i)+"天" for i in f_l]
plt.xticks(f_l,f)
plt.xlabel("天数")
plt.ylabel("温丽芬")
# plt.plot(pf,label="loi")
plt.legend()
plt.show()



