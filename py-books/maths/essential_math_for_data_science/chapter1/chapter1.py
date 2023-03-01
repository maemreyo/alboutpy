import sympy
from sympy.plotting import plot3d

x = sympy.symbols('x')
# ================================================================
# Plot a function
f = 2 * x + 1
sympy.plot(f)

# ================================================================
# Summations
summation = sum(2 * i for i in range(1, 6))

# ================================================================
# Exponents
expression = x ** 2 / x ** 5  # x**(-3)

# ================================================================
# Logarithms
y = sympy.log(8, 2)  # 3

# ================================================================
# Derivative
f = x ** 2
dx_f = sympy.diff(f)  # 2*x

u, v = sympy.symbols('x y')
f = 2 * x ** 3 + 3 * y ** 3

dx_f = sympy.diff(f, x)  # 6*x**2
dy_f = sympy.diff(f, y)  # 9*y**2

plot3d(f)

# The chain rule
z = (x ** 2 + 1) ** 3 - 2
dz_dx = sympy.diff(z, x)  # 6*x*(x**2 + 1**2

# =================================================================
# Integrals
f = x ** 2 + 1
area = sympy.integrate(f, (x, 0, 1))  # 4/3
