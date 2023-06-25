import numpy as np

# 1.where
# arr1 = np.arange(12).reshape(3,4)
# # where 函数 可以用作判断 where(condition, x=None, y=None) 有返回值
# arr2 = np.where(arr1>6,1,np.where(arr1>3,2,-2))
#
# print(arr2)

# 数组与标量运算      列数一定要相同 + - * / 都可
arr3 = np.array([[1,-2,-3],[1,2,3]])
arr4 = np.array([[4,5,6],[4,5,6]])

# 通用函数(ufunc) square sqrt abs add minimum maximum modf
print(np.square(arr4))
# [[16 25 36]
#  [16 25 36]]
print(np.sqrt(arr4))
# [[2.         2.23606798 2.44948974]
#  [2.         2.23606798 2.44948974]]
print(np.abs(arr3))
# [[1 2 3]
#  [1 2 3]]
print(np.add(arr4,arr3))
# [[5 3 3]
#  [5 7 9]]
print(np.minimum(arr4,arr3))
# [[ 1 -2 -3]
#  [ 1  2  3]]
print(np.maximum(arr4,arr3))
# [[4 5 6]
#  [4 5 6]]
print(np.modf(arr4))
# (array([[0., 0., 0.],
#        [0., 0., 0.]]), array([[4., 5., 6.],
#        [4., 5., 6.]]))


# 基本数组统计方法
print(arr4.sum())
# 30
print(arr4.mean())
# 5.0
print(arr4.std())
# 0.816496580927726
print(arr4.var())
# 0.6666666666666666
print(arr4.min())
# 4
print(arr4.max())
# 5
print(arr4.argmin())
# 0
print(arr4.argmax())
# 2
print(arr4.cumsum())
# [ 4  9 15 19 24 30]
print(arr4.cumprod())
# [    4    20   120   480  2400 14400]

# 排列 sort
# print(arr4.reshape(6).sort())  要搞

#  集合运算

print(np.unique(arr4))
# [4 5 6]
print(np.intersect1d(arr4,arr3))
# []
print(np.union1d(arr4,arr3))
# [-3 -2  1  2  3  4  5  6]
print(np.in1d(arr3,arr4))
# [False False False False False False]
print("*"*40)
print(np.setdiff1d(arr4,arr3))
# [4 5 6]
print(np.setxor1d(arr3,arr4))
# [ 1 -3 -2  2  3  4  5  6]

# 数组的存储 np.savetxt
arr5 = np.arange(16).reshape(4,4)
np.savetxt("we.csv",arr5,fmt="%d",delimiter=",")
uo = np.loadtxt("we.csv",delimiter=",")
print(uo)

print("*"*100)
arr1 = np.arange(6)
arr1.reshape(2,3)
arr2 = np.arange(6)
arr2.resize(2,3)
print(arr2.flatten())
print(arr1)
print(np.hstack([arr2.flatten(),arr1]))
print(np.concatenate((arr2.flatten(),arr1),axis=None))