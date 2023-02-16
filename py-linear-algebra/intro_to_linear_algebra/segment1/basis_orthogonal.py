import numpy as np

i = np.array([1, 0])
j = np.array([0, 1])

ortho = np.dot(i, j)
print("ortho", ortho)