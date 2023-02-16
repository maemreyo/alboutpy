# Chapter 7

## 1. Dictionary Default Values
```python
name_for_userid = {
    1: 'Alice',
    2: 'Bob',
    3: 'Jack',
}

def greeting(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there!')
```
- Avoid explicit `key in dict` checks when testing for membership.
- EAFP-style exception handling or using the built-in `get()` method is preferable.
- In some cases, the `collections.defaultdict` class from the standard library can also be helpful.

## 2. Sorting Dictionaries For Fun and Profit
```python
import operator

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

sorted(xs.items()) # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
sorted(xs.items(), key=lambda x: x[1]) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
sorted(xs.items(), key=lambda x: x[1], reverse=True) # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
sorted(xs.items(), key=operator.itemgetter(1)) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```
- When creating sorted "views" of dictionaries and other collections, you can influence the sort order with a _key func_.
- _Key funcs_ are an important concept in Python. The most frequently used ones were even added to the `operator` module
in the standard library.
- Functions are first-class citizens in Python. This is a powerful feature you’ll find used everywhere in the language.

## 3. Emulating Switch/Case Statements With Dicts
```python
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

dispatch_dict('mul', 2, 8) # 16
dispatch_dict('unknown', 2, 8) # None
```

- Python doesn't have switch/case statement. But in some cases you can avoid long `if`-chains with a dictionary-based
dispatch table.
- Once again, Python's first-class functions prove to be a powerful tool. But with great power comes great responsibility.

## 4. The Craziest Dict Expression in the West
```python
craziest = {True: 'yes', 1: 'no', 1.0: 'maybe'} # { True: 'maybe' }

# True == 1 == 1.0 => True
# (hash(True), hash(1), hash(1.0)) => (1, 1, 1) => Key collision 
```
- Dictionaries treat keys as identical if their `__eq__` comparison result says they're equal and their hash values are the same.
- Unexpected dictionary key collisions can and will lead to surprising results.

## 5. So Many Ways to Merge Dictionaries
```python
xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

zs = {}
zs.update(xs)
zs.update(ys)

cs = {}
cs = { **xs, **ys }
```

- In Python 3.5 and about you can use the `**`-operator to merge multiple dictionary objects into one with a single
expression, overwriting existing keys left-to-right.
- To stay compatible with older versions of Python, you might want to use the built-in dictionary `update()` method instead.

## 6. Dictionary Pretty-Printing
```python
import json
import pprint

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

str(mapping) # {'b': 42, 'c': 12648430, 'a': 23}
json.dumps(mapping, indent=4, sort_keys=True)
# {
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }

pprint.pprint(mapping) # {'a': 23, 'b': 42, 'c': 12648430, 'd': set([1, 2, 3])}
```

- The default to-string conversion for dictionary objects in Python can be difficult to read.
- The `pprint` and `json` module are "higher-fidelity" options build into the Python standard library.
- Be careful with using `json.dumps()` and non-primitive keys and values as this will trigger a `TypeError`.
