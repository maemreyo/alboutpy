import numpy as np

x = np.array([25, 2, 5])
print(x)
print(len(x))
print(x.shape)
print(type(x))
print(x[0])
print(type(x[0]))

y = np.array([[25, 2, 5]])
print(y, y.shape)

y_t = y.T
print(y_t, y_t.shape)
print(y_t.T)

z = np.zeros(3)
print(z, z.shape)