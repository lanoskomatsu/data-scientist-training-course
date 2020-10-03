import numpy as np
import numpy.random as random
# %precision 3

data = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])

print(data.dtype)

print(data * 2)
print(data ** 2)
print(data / 2)


print(data)
data.sort()
print(data)

data[::-1].sort()
print(data)

print(data.min())
print(data.max())
print(data.sum())
print(data.cumsum())
print(data.cumsum() / data.sum())

random.seed(0)
print(random.randn(10))


data = np.array([9,2,3,4,10,6,7,8,1,5])
print(random.choice(data,10))
print(random.choice(data,10,replace = False))

random.seed(1)
print(random.choice(data,10))
print(random.choice(data,10,replace = False))

print(np.arange(9))
data1 = np.arange(9).reshape(3,3)
print(data1)

data2 = np.arange(9, 18).reshape(3,3)
print(data2)
x = np.dot(data1, data2)
print(x)
print(data1 * data2)

print(np.zeros((2, 3), dtype = np.int64))
print(np.ones((2, 3), dtype = np.float64))
