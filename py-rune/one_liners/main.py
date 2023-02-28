# Useful one-liners

# Swap two variables
a = 10
b = 20

a, b = b, a

# Reverse a List
l = [1, 2, 3, 4]

new_list = l[::-1]

# Calculate the mode of a list
l = [1, 3, 2, 5, 2, 2, 5, 4]

max_fre = max(set(l), key=l.count)  # 2 (three times)

# Strip lines for start and end spaces and remove new lines
# lines = [line.strip() for line in lines]

# Multiple variable assignments
a, b, c = 4.4, 'Awesome', 7

# Convert a string into a number
int('27')

# Type casting a list items
l = ['12', '23', '24', '25', '26']
items = [int(item) for item in l]

# Find the square root of a number
4 ** .5

# Find the qube root of a number
27 ** (1 / 3)

# Get the absolute value of a number
abs(-27)

# Round a number to n digits
round(23.3213123, 2)

# Create a list of numbers in specific range
list(range(7, 21))

# Calculate the average of a list
l = [1, 2, 3, 4, 5]

sum(l) / len(l)

# If-else assignments
x = 19

v = 10 if x < 20 else 20

# Flatten the list of lists
l = [[1, 2], [3, 4], [5, 6], [7, 8]]
flatten = [j for i in l for j in i]
