# Basic Tensor Arithmetic
"""
    Adding or multiplying with scalar applies operation to all elements and tensors shape is retained.
"""
import torch

X = torch.tensor([[5, 10], [10, 20], [50, 100]])
print("X: <<<", X)

print("X*2: <<<", X*2)
print("X*2+2: <<<", X*2+2)
print("X+2: <<<", X+2)

A = X + 2
print("A: <<<", A)
print("A + X: <<<", A + X)
print("A * X: <<<", A * X)