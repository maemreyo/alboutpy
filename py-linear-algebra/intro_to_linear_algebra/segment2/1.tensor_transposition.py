# Tensor transposition
"""
    - Transpose of scalar is itself
    - Transpose of vector is .. converts column to row (and vice versa)
    - Scalar and vector transposition are special cases of matrix transposition:
        + Flip of axes over main diagonal: X_T[i][j] = X[j]][i]
"""
import torch

X = torch.tensor([[25, 2], [5, 26], [3, 7]])
print("X: ", X)

# Transpose a tensor
X_T = X.T
print("X_T: ", X_T)