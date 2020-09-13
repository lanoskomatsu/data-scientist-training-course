import numpy as np

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