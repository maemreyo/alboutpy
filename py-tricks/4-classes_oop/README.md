# Chapter 4: Classes & OOP

## 1. Object Comparison: ```is``` and ```==```
- An ```is``` expression evaluates to ```True``` if two variables point to the same object (identical).
- An ```==``` expression evaluates to ```True``` if the objects referred to by the variables are equal (have the same contents).
```python
a = [1, 2, 3]
b = a
c = list(a)

a == b #=> True
a is b #=> True

a == c #=> True
a is c #=> False
```

## 2. String Conversion (Every Class Needs a __repr__)
- You can control to-string conversion in your own classes using the ```__str__``` and ```__repr__``` "dunder" methods.
- The result of ```__str__``` should be readable. The result ```__repr__``` should be unambiguous.
- Always add a ```__repr__``` to your classes. The default implementation for ```__str__``` just calls ```__repr__```.
- Use ```__unicode__``` instead of ```__str__``` in Python 2.

## 3. Defining Your Own Exception Classes
- Defining your own exception types will state your code's intent more clearly and make it easier to debug.
- Derive your custom exceptions from Python's built-in ```Exception``` class or from more specific exception classes
like ```ValueError``` or ```KeyError```.
- You can use inheritance to define logically grouped exception hierarchies.
```python
def validate(name):
    if len(name) < 10:
        raise ValueError

class BaseValidationError(ValueError):
    pass

class NammTooShortError(BaseValidationError):
    pass
class NammTooLongError(BaseValidationError):
    pass

username = "Jame"    

try:
    validate(username)
except BaseValidationError as err:
    pass
```

## 4. Cloning Objects for Fun and Profit
For compound objects like lists, dicts, and sets, there's an important difference between *shallow* and *deep* copying:
- A *shallow copy* means constructing a new collection object and then populating it with references to the child objects
found in the original. In essence, a shallow copy is only ***one level deep***. The copying process does not recurse and
therefore won't create copies of the child objects themselves.
- A *deep copy* makes the copying process recursive. It means first constructing a new collection object and then recursively
populating it with copies of the child objects found in the original. Copying an object this way walks the whole object
tree to create a fully independent clone of the original object and all of its child objects.

### Making Shallow Copies
```python
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) # Make a shallow copy

xs.append(['new sublist']) # => [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new sublist']]
ys # => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

xs[1][0] = 'X'
xs # => [[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new sublist']]
ys # => [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
```

### Making Deep Copies
```python
import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)

xs # => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs # => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

xs[1][0] = 'X'
xs # => [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
zs # => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Copying Arbitrary Objects
Using ```copy``` module to make a shallow or deep copy

### Key takeaways
- Making a shallow copy of an object won't clone child objects. Therefore, the copy is not fully independent or the original.
- A deep copy of an object will recursively clone child objects. The clone is fully independent of the original, but creating a deep copy is slower.
- You can copy arbitrary objects (including custom classes) with the ```copy``` module.

## 5. Abstract Base Classes Keep Inheritance in Check

## 6. What Namedtuples are Good For

## 7. Class vs Instance Variable Pitfalls

## 8. Instance, Class, and Static Methods Demystified
































