# 1. Covering Your A** With Assertions
## Assert in Python - An example
```python
def apply_discount(product, discount):
    price = int(product['price'] * (1 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Lining', 'price': 100}
print(apply_discount(shoes, 0.25))
print(apply_discount(shoes, 2.0))
```
## Keep in mind
- The goal of using assertions is to let developers find the root cause of a bug more quickly.
- An assertion error should never be raised unless there's a bug in your program.

## Notice for usage
- Don't use `assert` for data validation
- Asserts that never fail

## Key takeaways
- Python's `assert` statement is a debugging aid that tests a condition as an internal self-check in your program.
- Asserts should only be used to help developers identify bugs. They're not a mechanism for handling run-time errors.
- Asserts can be globally disabled with an interpreter setting.

# 2. Complacent Comma Placement
A handy top for when you're adding and removing items from a list, dict, or set constant in Python: *Just end all your 
line with a comma*.

## Key takeaways
- Smart formmating and comma placement can make your list, dict, or set constants easier to maintain.
- Python's string literal concatenation feature can work to your benefit, or introduce hard-to-catch bugs.

# 3. Context Managers And The ```with``` Statement
- ```with``` is a highly useful feature that can help you write cleaner and more readable Python code.
- It helps simplify some common resources management patterns by abstracting their functionality and allowing them
to be factored out and reused.
- It also helps you avoid bugs or leaks by making it practically impossible to forget to clean up or release a resource
when it's no longer needed.

For example:
```python
with open('hello.text', 'w') as f:
    f.write('hello, world!')
```
Internally, the above code sample translates to something like this:
```python
f = open('hello.text', 'w')
try:
    f.write('hello, world!')
finally:
    f.close()
```
So instead of having to write an explicit ```try...finally``` statement each time, using the ```with``` statement take 
care of that for us.

## Supporting ```with``` in your own objects
### Self-implementing your management
```python
class ManagedFile:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
```

### Using the library
```python
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()
        
        
with managed_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')
```

## Key takeaways
- The ```with``` statement simplifies exception handing by encapsulating standard uses of ```try...finally``` statements.
- Most commonly it is used to manage the safe acquisition and release of system resources.
Resources are acquired by the ```with``` statement and released automatically when execution leaves the ```with``` context.
- Using ```with``` statements effectively can help you avoid resource leaks and make your code easier to read.

# 4. Underscores, Dunders, and More
Let's discuss the following five underscore patterns and naming conventions, and how they affect the behavior of your Python programs:
- Single Leading Underscore: ```_var```
- Single Trailing Underscore: ```var_```
- Double Leading Underscore: ```__var```
- Double Leading and Trailing Underscore: ```__var__```
- Single Underscore: ```_```

## 4.1. Single Leading Underscore: ```_var```
It is a Python naming convention that indicates a name is meant for internal use.
It is generally not enforced by the Python interpreter and is only meant as a hint to the programmer.

## 4.2. Single Trailing Underscore: ```var_```
Sometimes the most fitting name for a variable is already taken by a keyword in the Python language.
Therefore, names like ```class_``` or ```def``` cannot be used as variable names. 
In this case, you can append a single underscore to break the naming conflict:
```python
def make_object(name, class_):
    pass
```
In summary, a single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords. 
This convention is defined and explained in PEP 8.

## 4.3. Double Leading Underscore: ```__var```
- A double underscore prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming
conflicts in subclasses.
- This is also called ***name mangling***--the interpreter changes the name of the variable in a way that makes it harder
to create collisions when the class is extended later.

*Note: dunder stands for "double underscore""*

## 4.4. Double Leading and Trailing Underscore: ```__var__```
- Name mangling is *not* applied if a name *starts and ends* with double underscore.
- Avoid collisions with future changes to the Python language.

## 4.5. Single Underscore: ```_```
- A single stand-alone underscore is sometimes used as a name to indicate that a variable is temporary or insignificant.
- Use it in unpacking expressions as a "don't care" variable to ignore particular variables.
- Represents the result of the last expression evaluated by the interpreter.
- It's also handy if you're constructing objects on the fly and want to interact with them without assigning them a name first.

## Key takeaways
- Single Leading Underscore: Naming convention indicating a name is meant for internal use. Generally not enforced by
the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only.
- Single Trailing Underscore: Used by convention to avoid naming collisions with Python keywords.
- Double Leading Underscore: Triggers name mangling when used in a class context. Enforced by the Python interpreter.
- Double Leading and Trailing Underscore: Indicates special methods defined by the Python language. Avoid this naming
scheme for your own attributes.
- Single Underscore: Sometimes used as a name for temporary or insignificant variables. Also, it represents the result
of the last expression in a Python REPL session.

# 5. A Shocking Truth About String Formatting
## 5.1. "Old style" string formatting
```python
name = 'Bob'
'Hello, %s' % name
```

## 5.2. "New style" string formatting
```python
name = 'Bob'
'Hello, {}'.format(name)
```

## 5.3. Literal string interpolation (Python 3.6+)
```python
name = 'Bob'
f'Hello, {name}'
```

## 5.4. Template strings
```python
from string import Template
name = 'Bob'
t = Template('Hey, $name!')
t.substitute(name=name)
```

## Key takeaways
### Rule of thumb
> If your format string are user-supplied, use Template Strings to avoid security issues. Otherwise, use Literal String
Interpolation if you're on Python 3.6+, and "New Style" String Formatting if you're not.
- Perhaps surprisingly, there's more than one way to handle string formatting in Python.
- Each method has its individual pros and cons. Your use case will influence which method you should use.
- If you're having trouble deciding which string formatting method to use, try to read the String Formatting Rule of Thumb.

# 6. "The Zen of Python" Easter Egg
## The Zen of Python, by Tim Peters
> Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one—and preferably only one—obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let’s do more of those!