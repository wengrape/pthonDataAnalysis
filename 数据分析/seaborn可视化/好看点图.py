import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = pd.read_csv("tips.csv")
print(data.describe())

# sns.relplot(x="total_bill",y="tip",data=data,hue="day",col="smoker",row="time")
# sns.lmplot(x="total_bill",y="size",col="smoker",row="time",hue="day",data=data)

# plt.subplot(2,2,4)
# sns.stripplot(x="total_bill",y="day",data=data)
sns.boxplot(x="total_bill",y="day",data=data)
plt.savefig(fname="seaborn可视化")
plt.show()
