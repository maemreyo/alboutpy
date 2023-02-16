# 1. Python's Functions Are First-Class
## Functions are objects
```python
def yell(content):
    return content.upper() + '!'

yell("Hello") # => 'HELLO!'

bark = yell
bark('woof') # => 'WOOF!'

del yell
yell("hello?") # NameError: "name 'yell' is not defined"

bark('hey') # 'HEY!'

bark.__name__ # 'yell'
```

## Functions can be stored in data structures
## Functions can be passed to other functions
## Functions can be nested
## Functions can capture local state (closure)
## Objects can behave like functions

## Key takeaways
- Everything in Python is an object, including functions. You can assign them to variables, store them in data structures,
and pass or return them to and from other functions (first-class functions).
- First-class functions allow you to abstract away and pass around behavior in your programs.
- Functions can be nested and they can capture and carry some of the parent function's state with them. Functions that do
this are called closures.
- Objects can be made callable. In many cases this allows you to treat them like functions.

# 2. Lambdas Are Single-Expression Functions
- The ```lambda``` keyword in Python provides a shortcut for declaring small anonymous functions.
- Lambda functions behave just like regular functions declared with the ```def``` keyword.
- They can be used whenever function objects are required.
```python
add = lambda x, y: x + y
add(5, 3) # => 8

(lambda x, y: x + y)(5, 3) # => 8
```
- Executing a lambda function evaluates its expression and then automatically returns the expression's result,
so there's always an *implicit* return statement. So that's why some people refer to lambdas as *single expression functions*

## Lambdas you can use
For sorting:
```python
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
sorted(tuples, key=lambda x: x[1]) # => [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]
```

## Maybe you shouldn't
```python
# Harmful:
list(filter(lambda x: x % 2 == 0, range(16))) # => [0, 2, 4, 6, 8, 10, 12, 14]

# Better:
[x for x in range(16) if x % 2 == 0] # => [0, 2, 4, 6, 8, 10, 12, 14]
```

## Key takeaways
- Lambda functions are single-expression functions that are not necessarily bound to a name (anonymous)
- Lambda functions can't use regular Python statements and always include an implicit return statement.
- Always ask yourself: *Would using a regular (named) function or a list comprehension offer more clarify?*

# 3. The Power of Decorators
Use cases:
- Logging
- Enforcing access control and authentication
- Instrumentation and timing functions
- Rate-limiting
- Caching, and more

## Python Decorator Basics
```python
# The simplest decorator
def null_decorator(func):
    return func

# The usage example
def greet():
    return 'Hello!'

greet = null_decorator(greet)
greet() # => 'Hello!'

@null_decorator
def say_greet():
    return 'Hello there!'

greet() # => 'Hello there!'
```

## Decorators Can Modify Behavior
## Applying Multiple Decorators to a Function
```python
def strong(func):
    def wrapper():
            return '<strong>' + func() + '</strong>'
        return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello!'
```

## Decorating Functions That Accept Arguments
```python
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
                f'with {args}, {kwargs}')
    
        original_result = func(*args, **kwargs)
    
        print(f'TRACE: {func.__name__}() '
                f'returned {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

say('Jane', 'Hello, World')
# 'TRACE: calling say() with ("Jane", "Hello, World"), {}'
# 'TRACE: say() returned "Jane: Hello, World"'
# 'Jane: Hello, World'
```

## How to write "debuggable" decorators
Recommend that you use ```functools.wraps``` in all of the decorators you write yourself. 
It doesn't take much time and it will save you (and others) debugging headaches down the road.

## Key takeaways
- Decorators define reusable building blocks you can apply to a callable to modify its behavior without
permanently modifying the callable itself.
- The ```@``` syntax is just a shorthand for calling the decorator on an input function.
Multiple decorators on a single function are applied bottom to top (decorator stacking).
- As a debugging best practice, use the ```functools.wraps``` helper in your own decorators
to carry over metadata from the undecorated callable to the decorated one.
- Just like any other tool in the software development toolbox, decorators are not a cure-all
and they should not be overused. It's important to balance the need of "get stuff done" with the 
goal of "not getting tangled up in a horrible, unmaintainable mess of a code base."

# 4. Fun with *args and **kwargs
- *args and **kwargs let you write functions with a variable number of arguments in Python
- *args collects extra arguments as a tuple.
- **kwargs collects extra keyword arguments as a dictionary.
- The actual syntax is * and **. Calling them args and kwargs is just a convention (and one you should stick to)
```python
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo() # => TypeError: "foo() missing 1 required positional arg: 'required'"
foo('hello') # => hello
foo('hello', 1, 2, 3) # => hello (1, 2, 3)
foo('hello', 1, 2, 3, key1='value', key2=999) # => hello (1, 2, 3) {'key1': 'value', 'key2': 999}
```
# 5. Function Argument Unpacking
- The * and ** operator can be used to "unpack" function arguments from sequences and dictionaries.
- Using argument unpacking effectively can help you write more flexible interface for your modules and functions.
```python
def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

tuple_vec = (1, 0 ,1)
list_vec = [1, 0, 1]
dic_vec = { 'y': 0, 'z': 1, 'x': 1 }

print_vector(*tuple_vec) # => <1, 0, 1>
print_vector(*list_vec) # => <1, 0, 1>
print_vector(*dic_vec) # => <y, z, x>
print_vector(**dic_vec) # => <1, 0, 1>
```

# 6. Nothing to Return Here
- If a function doesn't specify a return value, it returns ```None```. Whether to explicitly return None is a stylistic decision.
- This is a core Python feature but your code might communicate its intent more clearly with an explicit ```return None``` statement.