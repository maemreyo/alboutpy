import numpy as np
X = np.array([[25, 2], [5, 26], [3, 7]])

print("X", X)
print("X.shape", X.shape)
print("X.size", X.size)
print("col 1", X[:, 0])
print("col 2", X[:, 1])
print("row 3", X[2, :])
