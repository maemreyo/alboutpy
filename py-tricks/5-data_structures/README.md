# Chapter 5: Common Data Structures in Python

## 1. Dictionaries, Maps, and Hashtables
### ```dict``` - Your Go-To Dictionary
- For most use cases, Python's built-in dictionary implementation will do everything you need.
Dictionaries are highly optimized and underlie many parts of the language. For example class attributes and variables
in a stack frame are both stored internally in dictionaries.
- Provides the performance characteristics you'd expect: O(1) time complexity for
lookup, insert, update, and delete operations in the average case.

### ```collections.OrderedDict``` - Remember the Insertion Order of Keys
- If key order is important for your algorithm to work, it's best to communicate this clearly by explicitly using the 
```OrderDict``` class.
- ```OrderedDict``` is not a built-in part of the core language and must be imported from the ```collections``` module
in the standard library.

### ```collections.defaultdict``` - Return Default Values for Missing Keys
- The ```defaultdict``` class is another dictionary subclass that accepts a callable in its constructor whose return
value will be used if a requested key cannot be found.

### ```collections.ChainMap``` - Search Multiple Dictionaries as a Single Mapping
- The ```collections.ChainMap``` data structure groups multiple dictionaries into a single mapping.
- Lookups search the underlying mappings one by one until a key is found.
- Insertions, updates, and deletions only affect the first mapping added to the chain.

### ```types.MappingProxyType``` - A Wrapper for Making Read-Only Dictionaries
- ```MappingProxyType``` is a wrapper around a standard dictionary that provides a read-only view into the wrapped 
dictionary's data.
- It can be used to create immutable proxy versions of dictionaries.

### Dictionaries in Python: Conclusion
### Key takeaways
- Dictionaries are the central data structure in Python.
- The built-in dictionary type will be "good enough" most of the time.
- Specialized implementations, like read-only or ordered dicts, are available in Python standard library.

## 2. Array Data Structures
### ```list``` - Mutable Dynamic Arrays
- Python's lists are implemented as *dynamic arrays* behind the scenes.
- This means a list allows elements to be added or removed, and the list will automatically adjust the backing store that 
holds these elements by allocating or releasing memory.

### ```tuple``` - Immutable Containers
- Python's tuple objects are immutable.
- This means elements can't be added or removed dynamically, all elements in a tuple must be defined at creation time.

### ```array.array``` - Basic Typed Arrays
- Arrays created with the ```array.array``` class are mutable and behave similarly to lists, except for one important difference:
they are "typed arrays" constrained to a single data type.
- Useful if you need to store many elements of the same type.

### ```str``` - Immutable Arrays of Unicode Characters
- Python 3.x uses ```str``` to store textual data as immutable sequences of Unicode characters. That means a ```str```
is an immutable array of characters.

### ```bytes``` - Immutable Arrays of Single Bytes
- Bytes objects are immutable sequences of single bytes (integers in the range 0 <= x <= 255).
- They're similar to ```str``` objects, and you can also think of them as immutable arrays of bytes.
- Like strings, ```bytes``` have their own literal syntax for creating objects, and they're space-efficient. 
- Bytes objects are immutable, but unlike strings, there's dedicated "mutable byte array" data type called ```bytearray``` 
that they can be unpacked into.

### ```bytearray``` - Mutable Arrays of Single Bytes
- The ```bytearray``` type is a mutable sequence of integers in the range 0 <= x <= 255.
- They're closely related to ```bytes``` objects with the main difference being that ```bytearray``` can be modified freely
- Bytearrays can be converted back into immutable bytes objects.

### Key takeaways
Here's what our choices come down to:
- **You need to store arbitrary objects, potentially with mixed data types?** Use a ```list``` or a ```tuple```, depending
on whether you want an immutable data structure or not.
- **You have numeric data and tight packing and performance is important?** Try out ```array.array``` and see if it does
everything you need. Also, consider going beyond the standard library and try out packages like *NumPy* or *Pandas*.
- **You have textual data represented as Unicode characters?** Use Python's built-in ```str```. If you need a "mutable string"
, use a ```list``` of characters.
- **You want to store a contiguous block of bytes?** Use the immutable ```bytes``` types, or ```bytearray``` if you need 
a mutable data structure.

## 3. Records, Structs, and Data Transfer Objects
### ```dict``` - Simple Data Objects
- Python dictionaries store an arbitrary number of objects, each identified by a unique key.
- Dictionaries are also often called *maps* or *associative arrays* and allow for the efficient lookup, insertion, and deletion
of any object associated with a given key.

### ```tuple``` - Immutable Groups of Objects
- Python's tuples are simple data structures for grouping arbitrary objects.
- Tuples are immutable, they cannot be modified once they've been created.

### Writing a Custom Class - More Work, More Control
### ```collections.namedtuple``` - Convenient Data Objects
- The ```namedtuple``` class available in Python 2.6+ provides an extension of the built-in ```tuple``` data type.
- Allows us to define reusable "blueprints" for records that ensure the correct field names are used.
- Namedtuple are immutable, just like regular tuples. This means you cannot add new fields ore modify existing fields
after the namedtuple instance was created.
- Each object stored in them can be accessed through a unique identifier. This frees you from having to remember integer
indexes, or resort to workarounds like defining integer constants as mnemonics for your indexes.
```python
from collections import namedtuple

p1 = namedtuple('Point', 'x y z')(1, 2, 3)
p2 = (1, 2, 3)

Car = namedtuple('Car', 'color mileage automatic')
car1 = Car('red', 3812.4, True)

print(car1) # => Car(color='red', mileage=3812.4, automatic=True)
print(car1.mileage) # => 3812.4
car1.mileage = 12 # => AttributeError
```

### ```typing.NamedTuple``` - Improved NamedTuples
- This class added in Python 3.6 is the younger sibling of the ```namedtuple``` class in the ```collections``` module.
- It is very similar to ```namedtuple```, the main difference being an updated syntax for defining new record types and
added support for type hints.
```python
from typing import NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

car1 = Car('red', 3812.4, True)

print(car1) # => Car(color='red', mileage=3812.4, automatic=True)
print(car1.mileage) # => 3812.4
car1.mileage = 12 # => AttributeError
```

### ```struct.Struct``` - Serialized C Structs
- The ```struct.Struct``` class converts between Python values and C structs serialized into Python ```bytes``` objects.

### ```types.SimpleNamespace``` - Fancy Attribute Access
- It's basically a glorified dictionary that allows attribute access and prints nicely. Attributes can be added, modified, and deleted freely.
```python
from types import SimpleNamespace

car1 = SimpleNamespace(
    color='red',
    mileage=3812.4,
    automatic=True,
)

print(car1) # => namespace(automatic=True, color='red', mileage=3812.4)
car1.mileage = 12
car1.windshield = 'broken'
del car1.automatic

print(car1) # => namespace(color='red', mileage=3812.4, windshield='broken')
```

### Key takeaways
Generally your decision will depend on your use case:
- **You only have a few (2-3) fields**: Using a plain tuple object may be okay if the field order is easy to remember or
field names are superfluous. For example, think of an (x, y, z) point in 3D space.
- **You need immutable fields**: In this case, plain tuples, ```collections.namedtuple``` and ```typing.NamedTuple``` 
would all make good options for implementing this type of data object.
- **You need to lock down field names to avoid typos**: ```collections.namedtuple```` and ```typing.NamedTuple``` are
your friends here.
- **You want to keep things simple**: A plain dictionary object might be a good choice due to the convenience syntax that
closely resembles JSON.
- **You need full control over your data structure**: It's time to write a custom class with ```@property``` setters and getters.
- **You need to add behavior (methods) to the object**: You should write a custom class, either from scratch or by extending
```collections.namedtuple``` or ```typing.NamedTuple```.
- **You need to pack data tightly to serialize it to disk or to send it over the network**: Time to read up on ```struct.Struct```
because this is a great use case for it.

## 4. Sets and Multisets
- A *set* is an unordered collection of objects that does not allow duplicate elements.
- Sets are used to quickly test a value for membership in the set, to insert or delete new values from a set, and to 
compute the union or intersection of two sets.

### ```set``` - Your Go-To Set
- This is the built-in set implementation in Python.
- The ```set``` type is mutable and allows for the dynamic insertion and deletion of elements.
```python
vowels = { 'a', 'e', 'i', 'o', 'u' }
# 'e' in vowels # => True

letters = set('alice')
letters.intersection(vowels) # => { 'a', 'e', 'i' }

vowels.add('x')
len(vowels) # => 6
```

### ```frozenset``` - Immutable Sets
- It implements an *immutable* version of ```set``` that cannot be changed after it has been constructed.
- Frozensets are static and only allow query operations on their elements (no inserts or deletions).

```python
vowels = frozenset({ 'a', 'e', 'i', 'o', 'u' })
# vowels.add('p') # => AttributeError

d = { frozenset({ 1, 2, 3 }): 'hello' } # => 'hello'
```

### ```collections.Counter``` - Multisets
- The ```collections.Counter``` class in the Python standard library implements a multiset (or bag) type that allows
elements in the set to have more than one occurrence.
```python
from collections import Counter
inventory = Counter()

loot = { 'sword': 1, 'bread': 3 }
inventory.update(loot) # => Counter({'bread': 3, 'sword': 1})

more_loot = { 'sword': 1, 'apple': 1}
inventory.update(more_loot) # => Counter({'bread': 3, 'sword': 2, 'apple': 1})
```

### Key takeaways
- Sets are another useful and commonly used data structure included with Python and its standard library.
- Use the built-in ```set``` type when looking for a mutable set.
- ```frozenset``` objects are hashtable and can be used as dictionary or set keys.
- ```collections.Counter``` implements multiset or "bag" data structures.

## 5. Stacks (LIFOs)
- A stack is a collection of objects that supports fast *last-in, first-out* (LIFO) semantics for inserts and deletes.
- Unlike lists or arrays, stacks typically don't allow for random access to the objects they contain.
- The insert and delete operations are also called *push* and *pop*.

### ```list``` - Simple, Built-in Stacks
### ```collections.deque``` - Fast & Robust Stacks
- The ```deque``` class implements a double-ended queue that supports adding and removing elements from either end in 
O(1) time.
- Because deques support adding and removing elements from either end equally well, they can serve both as queues and as stacks.

### ```queue.LifoQueue``` - Locking Semantics for Parallel Computing
### Comparing Stack Implementations in Python
- ```list``` is backed by a dynamic array which makes it great for fast random access, but requires occasional resizing
when elements are added or removed. The list over-allocates its backing storage so that not every push or pop requires
resizing, and you get an amortized O(1) time complexity for these operations. But you do need to be careful to only insert
and remove items "from the right side" using ```append()``` and ```pop()```. Otherwise, performance slows down to O(n).
- ```collections.deque``` is backed by a doubly-linked list which optimizes appends and deletes at both ends and provides
consistent O(1) performance for these operations. Not only is its performance more stable, the ```deque``` class is also
easier to use because you don't have to worry about adding or removing items from "the wrong end".

### Key takeaways
- Python ships with several stack implementations that have slightly different performance and usage characteristics.
- ```collections.deque``` provides a safe and fast general-purpose stack implementation.
- The built-in ```list``` type can be used as a stack, but be careful to only append and remove items with ```append```
and ```pop``` in order to avoid slow performance.

## 6. Queues (FIFOs)
- A queue is a collection of objects that support fast *first-in, first-out* (FIFO) semantics for inserts and deletes.
- The insert and delete operations are sometimes called *enqueue* and *dequeue*. Unlike lists or arrays, queues typically
don't allow for random access to the objects they contain.

### ```list``` - Terrible Slow Queues
- It's possible to use a regular ```list``` as a queue but this is not ideal from a performance perspective. Lists are
quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all the other
elements by one, requiring O(n) time. Therefore, I would ***not recommend*** using a ```list``` as a makeshift queue in 
Python (unless you're only dealing with a small number of elements).

### ```collections.deque``` - Fast & Robust Queues
- The ```deque``` class implements a double-ended queue that supports adding and removing elements from either end in 
O(1) time.
- Because deques support adding and removing elements from either end equally well, they can serve both as queues and as 
stacks.
- Python's ```deque``` objects are implemented as doubly-linked lists. This gives them excellent and consistent performance
for inserting and deleting elements, but poor O(n) performance for randomly accessing elements in the middle of the stack.

### ```queue.Queue``` - Locking Semantics for Parallel Computing
- This queue implementation in the Python standard library is synchronized and provides locking semantics to support multiple concurrent
producers and consumers.
- The queue module contains several other classes implementing multiproducer/multi-consumer queues that are useful for parallel computing.

### ```multiprocessing.Queue``` - Shared Job Queues
- This is a shared job queue implementation that allows queued items
to be processed in parallel by multiple concurrent workers.38 Processbased parallelization is popular in CPython due to the global interpreter lock (GIL) that prevents some forms of parallel execution on a
single interpreter process.

### Key takeaways
- Python includes several queue implementations as part of the core language and its standard library.
- ```list``` objects can be used as queues, but this is generally not recommended due to slow performance.
- If you're not looking for parallel processing support, the implementation offerd by ```collections.deque``` is an
excellent default choice for implementing a FIFO queue data structure in Python. It provides the performance characteristics
you'd expect from a good queue implementation and can also be used as a stack (LIFO queue).

## 7. Priority Queues
- A priority queue is a container data structure that manages a set of record with totally-ordered keys to provide quick
access to the record with the smallest or largest key in the set.
- You can think of a priority queue as a modified queue: instead of retrieving the next element by insertion time, it
retrieves the *highest priority* element. The priority of individual elements is decided by the ordering applied to
their keys.
- Priority queues are commonly used for dealing with scheduling problems, for example, to give precedence to tasks with
higher urgency.

### ```list``` - Maintaining a Manually Sorted Queue
- You can use a sorted ```list``` to quickly identify and delete the smallest or largest element.
- The downside is that inserting new elements into a list is a slow O(n) operation.
- While the insertion point can be found in O(log n) time using ```bisect.insort``` in the standard library, this is
always dominated by the slow insertion step.
- Maintaining the order by appending to the list and re-sorting also takes at least O(n log n) time.
- Another downside is that you must manually take care of re-sorting the list when new elements are inserted. Then it's 
easy to introduce bugs by missing this step, and the burden is always on you, the developer.

### ```heapq``` - List-Based Binary Heaps
- This is a binary heap implementation usually backed by a plain ```list``` and it supports insertion and extraction of
the smallest element in O(log n) time.
- This module is a good choice for implementing priority queues in Python. Since ```heapq``` technically only provides a
min-heap implementation, extra steps must be taken to ensure sort stability and other features typically expected from 
a "practical" priority queue.

```python
import heapq

q = []

heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)

# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')
```

### ```queue.PriorityQueue``` - Beautiful Priority Queues
- This priority queue implementation uses heapq internally and shares the same time and space complexities.
- The difference is that ```PriorityQueue``` is synchronized and provides locking semantics to support multiple 
concurrent producers and consumers.

```python
from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)

# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')
```

### Key takeaways
- Python includes several priority queue implementations for you to use.
- queue.PriorityQueue stands out from the pack with a nice object-oriented interface and a name that clearly states 
its intent. It should be your preferred choice.
- If you’d like to avoid the locking overhead of queue.PriorityQueue, using the heapq module directly is also a good option.