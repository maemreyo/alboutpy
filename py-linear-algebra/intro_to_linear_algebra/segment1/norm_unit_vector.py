# Norm and Unit vectors
import numpy as np

vec = np.array([25, 2, 5])
print("vec", vec)

norm = (25**2 + 2**2 + 5**2)**(1/2)
print("norm", norm)

norm_ = np.linalg.norm(vec)
print("norm_", norm_)

# L1 Norm
l1_norm = np.abs(25) + np.abs(2) + np.abs(5)
print("l1_norm", l1_norm)

# Squared L2 Norm
squared_l2_norm = (25**2 + 2**2 + 5**2)
print("squared_l2_norm", squared_l2_norm)

# Max norm
max_norm = np.max([np.abs(25), np.abs(2), np.abs(5)])
print("max_norm", max_norm)

