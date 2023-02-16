# The Dot Product
"""
    - If we have two vectors (x and y) with the same length n, we can calculate the dot product between them.
    - We calculate products in an element-wise fashion and then sum reductively across the products to a scalar value.
    - The dot product is ubiquitous in deep learning: It is performed at every artificial neuron in a deep neural
    network, which maybe made up of millions (or orders of magnitude more) of these neurons.
"""
import numpy as np
import torch

x = np.array([25, 2, 5])
y = np.array([0, 1, 2])

dot = np.dot(x, y)
print("dot", dot)

x_pt = x.T
y_pt = y.T

dot_pt = np.dot(x_pt, y_pt)
print("dot_pt", dot_pt)

torch_dot = torch.dot(torch.tensor([25, 2, 5]), torch.tensor([0, 1, 2]))
print("torch_dot", torch_dot)