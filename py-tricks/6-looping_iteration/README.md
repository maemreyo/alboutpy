# Chapter 6: Looping & Iteration

## 1. Writing Pythonic Loops
- In Python, ```for-loops``` are really "for-each" loops that can iterate directly over items from a container or 
sequence, without having to look them up by index.
```python
items = []
for item in items:
    print(item)
```
- It's possible to write loops that keep a running index while avoiding the ```range(len(...))``` pattern. The
```enumerate()``` built-in helps you make those kinds of loops nice and Pythonic:
```python
items = []

for i, item in enumerate(items):
    print(f'{i}: {item}')
```

## 2. Comprehending Comprehensions
- The key to understanding list comprehensions is that they’re just forloops over a collection but expressed in a more 
terse and compact syntax.
```python
squares = [x * x for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = [x * x for x in range(10) if x % 2 == 0] # [0, 4, 16, 36, 64]
```
- Set comprehension
```python
set_com = { x * x for x in range(-9, 10) } # set([64, 1, 36, 0, 49, 9, 16, 81, 25, 4])
```
- Dictionary comprehension
```python
dict_com = { x: x * x for x in range(5) } # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Key takeaways
- Comprehension are a key feature in Python. Understanding and applying them will make your code much more Pythonic.
- Comprehensions are just fancy syntactic sugar for a simple ```for-loop``` pattern. Once you understand the pattern,
you'll develop an intuitive understanding for comprehensions.
- There are more than just list comprehension.

## 3. List Slicing Tricks and the Sushi Operator
- Python's list objects have a neat feature called *slicing*. You can view it as an extension of the square-brackets
indexing syntax.
- Slicing is commonly used to access ranges of elements within an ordered collection.
```python
lst = [1, 2, 3, 4, 5]

# lst[start:stop:step]
lst[1: 3: 1] # [2, 3]
lst[1:3] # [2, 3] # Default step: 1
lst[::2] # [1, 3, 5]
lst[::-1] # [5, 4, 3, 2, 1]
```

### Key takeaways
- The ```:``` operator is not only useful for selecting sublists of elements within a list. It can also be used to clear
, reverse, and copy lists.
- But be careful, that functionality borders on the arcane for many Python developers. Using it might make your code
less maintainable for everyone else on your team.

## 4. Beautiful Iterators
- Iterators provides a sequence interface to Python objects that's memory efficient and considered Pythonic. Behold
the beauty of the for-in loop.
- To support iteration an object needs to implement the iterator protocol by providing the ```__iter__``` and 
```__next__``` dunder methods.
- Class-based iterators are only one way to write iterable objects in Python. Also consider generators and generator 
expressions.

## 5. Generators Are Simplified Iterators
- Generator functions are syntactic sugar for writing objects that support the iterator protocol. Generators abstract 
away much of the boilerplate code needed when writing class-based iterators.
- The `yield` statement allows you to temporarily suspend execution of a generator function and to pass back values 
from it
- Generators start raising `StopIteration` exceptions after control flow leaves the generator function by any means 
other than a yield statement.

## 6. Generator Expressions
- Generator expressions are similar to list comprehensions. However, they don’t construct list objects. Instead, 
generator expressions generate values “just in time” like a class-based iterator or generator function would.
- Once a generator expression has been consumed, it can’t be restarted or reused.
- Generator expressions are best for implementing simple “ad hoc” iterators. For complex iterators, it’s better to
write a generator function or a class-based iterator.

## 7. Iterator Chains
- Generators can be chained together to form highly efficient and maintainable data processing pipelines.
- Chained generators process each element going through the chain individually.
- Generator expressions can be used to write concise pipeline definitions, but this can impact readability.