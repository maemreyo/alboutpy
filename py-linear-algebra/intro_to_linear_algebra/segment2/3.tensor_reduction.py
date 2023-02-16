# Tensor Reduction
"""
    Calculating the sum across all elements of a tensor is a common operation.
"""
import torch

X = torch.tensor([[5, 10], [10, 20], [50, 100]])
print("X: <<<", X)

print("X.sum(): ", X.sum())
print("torch.sum(X.T): ", torch.sum(X.T))
print("X.sum(axis=0): ", X.sum(axis=0))
print("X.sum(axis=1): ", X.sum(axis=1))

"""
    Many other operations can be applied with reduction along all or a selection of axes
        - maximum
        - minimum
        - mean
        - product
"""