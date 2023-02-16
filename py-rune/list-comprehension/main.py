# List comprehension for filtering
temperatures = [12, 32, 34, 28, 14, 15, 20, 22, 25, 29]

print("Result: ", [t for t in temperatures if 18 <= t < 25])

alphanumeric = ["47", "abcd", "21st", "n0w4y", "1337", "0kay"]

print("Result: ", [int(s) for s in alphanumeric if s.isdigit()])

# Combining lists
colors = ["RED", "BLUE", "GREEN", "WHITE", "BLACK"]
models = ["12", "12 Pro", "13", "13 Pro"]

print("Result: ", [(model, color) for model in models for color in colors])

# Finding common elements
class_a = ["A", "B", "C", "D", "E"]
class_b = ["H", "B", "E", "F", "G"]

print("Result: ", [c for c in class_a if c in class_b])

# Combining elements with the same position
names = ["John", "Josh", "Jame"]
surnames = ["Smith", "Wonder", "Singer"]
ages = ["22", "19", "20"]

print("Result:", [f"{name} {surnames} - {age}" for name, surnames, age in zip(names, surnames, ages)])


# Convert vales
def convert_to_dol(eur):
    return round(eur * 1.19, 2)


prices = [22, 25.2, 19, 10, 100, 250, 23]

print("Result: ", [convert_to_dol(price) for price in prices])

# Frequency count
statement = "This is my home where I can do everything I like"

print("Result: ", {c: statement.count(c) for c in set(statement)})


# Generator
def return_next():
    for i in range(10):
        yield i


print("Result: ", [i for i in return_next()])
# List comprehension for filtering
temperatures = [12, 32, 34, 28, 14, 15, 20, 22, 25, 29]

print("Result: ", [t for t in temperatures if 18 <= t < 25])

alphanumeric = ["47", "abcd", "21st", "n0w4y", "1337", "0kay"]

print("Result: ", [int(s) for s in alphanumeric if s.isdigit()])

# Combining lists
colors = ["RED", "BLUE", "GREEN", "WHITE", "BLACK"]
models = ["12", "12 Pro", "13", "13 Pro"]

print("Result: ", [(model, color) for model in models for color in colors])

# Finding common elements
class_a = ["A", "B", "C", "D", "E"]
class_b = ["H", "B", "E", "F", "G"]

print("Result: ", [c for c in class_a if c in class_b])

# Combining elements with the same position
names = ["John", "Josh", "Jame"]
surnames = ["Smith", "Wonder", "Singer"]
ages = ["22", "19", "20"]

print("Result:", [f"{name} {surnames} - {age}" for name, surnames, age in zip(names, surnames, ages)])


# Convert vales
def convert_to_dol(eur):
    return round(eur * 1.19, 2)


prices = [22, 25.2, 19, 10, 100, 250, 23]

print("Result: ", [convert_to_dol(price) for price in prices])

# Frequency count
statement = "This is my home where I can do everything I like"

print("Result: ", {c: statement.count(c) for c in set(statement)})


# Generator
def return_next():
    for i in range(10):
        yield i


print("Result: ", [i for i in return_next()])
