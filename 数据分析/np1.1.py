import numpy as np

# 切片 左闭右开
arr1 = np.arange(9)
# 一维
# 取前5位
arr2 = arr1[:5]
print("arr2:", arr2)
# 取后5位
arr21 = arr1[-5:]
print("arr21:", arr21)
# 二维
arr1 = np.arange(9)
arr3 = arr1.reshape(3, 3)
# 三行三列
print("arr3:\n", arr3)
# 取第一行
arr4 = arr3[0]
print("arr4:\n", arr4)
# 取第二和第三行
arr41 = arr3[1:3]
print("arr41:\n", arr41)
# 取第一列
arr5 = arr3[:,0]
print("arr5:",arr5)
# 取第二和第三列
arr51 = arr3[:,1:3]
print("arr51:\n", arr51)
# 取第一行的第二列
arr6 = arr3[0,1]
print("arr6:\n", arr6)
# 取第二和第三行的第二和第三列
arr7 = arr3[1:3,1:3]
print("arr7:\n",arr7)
# 三维
arr = np.arange(12).reshape(2,2,3)
print("arr:\n",arr)
# 取第一个二维的第一行
aar1 = arr[0,0]
print("aar1:\n", aar1)
# 取第一个二维的第一列
aar2 = arr[0,:,0]
print("aar2:\n",aar2)
# 取第一个二维的第一行的第一列
aar3 = arr[0,0,0]
print("arr3:\n", aar3)
# 取第一和第二个二维的第一行
aar4 = arr[0:2,0]
print("aar4:\n",aar4)
# 取第一和第二个二维的第一列
aar5 = arr[0:2,:,0]
print("aar5:\n",aar5)
# 取第一和第二个二维的第一行的第一列
aar6 = arr[0:2,0,0]
print("aar6:\n",aar6)

