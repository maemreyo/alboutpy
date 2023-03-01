from numpy import array
from numpy.linalg import det

v = array([3, 2])
print(v)

# =================================================================
# Combining and scaling

v = array([3, 2])
w = array([2, -1])
v_plus_w = v + w

v = array([3, 1])
scaled_v = 2.0 * v
print(scaled_v)  # [6 2]

# =================================================================
# Matrix Vector Multiplication

# compose basis matrix with i-hat and j-hat
basis = array([[3, 0], [0, 2]])

# declare vector v
v = array([1, 1])

# create new vector
# by transforming v with dot product
new_v = basis.dot(v)

print(new_v)  # [3, 2]

# =================================================================
# Matrix Multiplication

# Transformation 1
i_hat1 = array([0, 1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()

# Transformation 2
i_hat2 = array([1, 0])
j_hat2 = array([1, 1])
transform2 = array([i_hat2, j_hat2]).transpose()

# Combine Transformations
combined = transform2 @ transform1
reversed_combined = transform1 @ transform2
# Test
print("COMBINED MATRIX:\n {}".format(combined))

v = array([1, 2])
print(combined.dot(v))  # [-1, 1]
print(reversed_combined.dot(v))  # [-2, 3]

# =================================================================
# Determinants

i_hat = array([3, 0])
j_hat = array([0, 2])

basis = array([i_hat, j_hat]).transpose()

determinant = det(basis)

print(determinant)  # prints 6.0

# ===
i_hat = array([-2, 1])
j_hat = array([3, -1.5])

basis = array([i_hat, j_hat]).transpose()

determinant = det(basis)

print(determinant)  # prints 0.0

# ==============================================================
# Inverse matrix

from sympy import *

# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72

A = Matrix([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

B = Matrix([
    44,
    56,
    72
])

X = A.inv() * B

print(X)  # Matrix([[2], [34], [-8]])

# ==============================================================
# Eigenvectors and Eigenvalues
from numpy import array, diag
from numpy.linalg import eig, inv

A = array([
    [1, 2],
    [4, 5]
])

eigenvals, eigenvecs = eig(A)

print("EIGENVALUES")
print(eigenvals)
print("\nEIGENVECTORS")
print(eigenvecs)

# EIGENVALUES [-0.46410162  6.46410162]
# EIGENVECTORS [[-0.80689822 -0.34372377] [ 0.59069049 -0.9390708 ]]

# ===
from numpy import array, diag
from numpy.linalg import eig, inv

A = array([
    [1, 2],
    [4, 5]
])

eigenvals, eigenvecs = eig(A)

print("EIGENVALUES")
print(eigenvals)
print("\nEIGENVECTORS")
print(eigenvecs)

print("\nREBUILD MATRIX")
Q = eigenvecs
R = inv(Q)

L = diag(eigenvals)
B = Q @ L @ R

print(B)

"""
EIGENVALUES
[-0.46410162  6.46410162]

EIGENVECTORS
[[-0.80689822 -0.34372377]
 [ 0.59069049 -0.9390708 ]]

REBUILD MATRIX
[[1. 2.]
 [4. 5.]]
"""
