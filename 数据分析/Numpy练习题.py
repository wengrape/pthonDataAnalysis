import numpy as np

print(np.__version__)

# arr1 = np.array([True])
# print(arr1)
print(np.full((3,3),False,dtype=np.bool))
print(np.arange(12).reshape(3,4).T)

arr1 = np.where(np.arange(12).reshape(3,4) % 2 ==0,0,np.arange(12).reshape(3,4))
print(arr1)
arr2 = (np.arange(12).reshape(3,4))

arr2[arr2 % 2 == 0]=0
print(arr2)

arr3 = np.random.random(size=10)
print(arr3)

n = np.arange(15)
n1 = np.where((n>=5) & (n<=10))
print(n1)

arr2 = (np.arange(12).reshape(3,4))
print(arr2[::-1,::-1])

a=1.2312
print("%.2f"%a)

print(np.unique(arr2))
print(arr2.max(axis=0))
print(arr2.min()-arr2.max())