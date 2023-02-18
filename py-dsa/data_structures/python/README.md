# Data Structures used in Algorithms (Python)
There are five various data structures that can be used to store collections:
- Lists: Ordered mutable sequences of elements
- **Tuples**: Ordered immutable sequences of elements
- **Dictionary**: Unordered bags of key-value pairs
- **Sets**: Unordered bags of elements
- **Data frames**: Two-dimensional structures to store two-dimensional data

## List
- A list is the main data structure used to store a mutable sequence of elements.
- The sequence of data elements stored in the list need not be of the same type.
- Utility functions
  - *List indexing*
  - *Negative indexing*
  - *List slicing*
  - *Nesting*
  - *Iteration*
- Lambda functions
  - *Filtering data*
  - *Data transformation*
  - *Data aggregation*
- The time complexity of lists can be summarized as follows using the Big O notation:

| Methods           | Time complexity |
| ----------------- | --------------- |
| Insert an element | O(1)            |
| Delete an element | O(n)            |
| Slicing a list    | O(n)            |
| Element retrieval | O(n)            |
| Copy              | O(n)            |

## Tuples
- Tuples are immutable (read-only) data structures.
- Elements within a tuple can be of different types.

| Method | Time Complexity |
| ------ | --------------- |
| append | O(1)            |

## Dictionary
- Holding data as key-value pairs is important especially in distributed algorithms.
- A collection of these key-value pairs is stored as a data structure called a *dictionary*.

| Methods              | Time complexity |
| -------------------- | --------------- |
| Get a value or a key | O(1)            |
| Set a value or a key | O(1)            |
| Copy a dictionary    | O(n)            |

## Sets
- A set is defined as a collection of elements that can be of different types.
- The defining characteristic of a set is that it only stores the distinct value of each element. If we try to add another redundant element, it will ignore that.
- Can have operations such as *unions* and *intersections*
  - ***Union operation***: combines all of the elements together of both sets.
  - ***Intersection operation***: give a set of common elements between the two sets.

| Methods           | Time complexity |
| ----------------- | --------------- |
| Add an element    | O(1)            |
| Remove an element | O(1)            |
| Copy              | O(n)            |

## DataFrames
- A DataFrame is a data structure used to store tabular data available in Python's `pandas` package.
- This is one of the most important data structures for algorithms and is used to process traditional structured data.
- Terminologies:
  - **Axis**: A single column or row of a DataFrame.
  - **Axes**: If there is more than one axis, they are called axes as a group.
  - **Label**: A DataFrame allows the naming of both columns and rows with a label.
- Two main ways of creating the subset of a DataFrame
  - Column selection
    - By column name
    - By position
  - Row selection
    - By position
    - By a filter

## Matrix
- A matrix is two-dimensional data structure with a fixed number of columns and rows. Each element of the matrix of a matrix can be referred to by its column and the row.
- Matrix operations
  - `transpose()`

## Abstract data types

### Vector
- A vector is a single dimension structure to store data.
- The most popular data structures in Python.
- Two ways of creating vectors in Python
  - Using a Python `list`
  - Using a `numpy` array

### Stacks
- A stack is a linear data structure to store a one-dimensional list.
- It can store items either LIFO or FILO manner.
- The defining characteristic of a stack is the way elements are added and removed from it.
- Operations related to the stacks:

| Operations | Description                                            |
| ---------- | ------------------------------------------------------ |
| isEmpty    | Returns true if the stack is empty                     |
| push       | adds a new element                                     |
| pop        | returns the element added most recently and removes it |

![stack_operations][stack_operations]

- Time complexity as the following table shows:

| Operations | Time Complexity |
| ---------- | --------------- |
| push       | O(1)            |
| pop        | O(1)            |
| size       | O(1)            |
| peek       | O(1)            |

- Practical example: Browser Undo and Forward a page

### Queues
- A queue stores *n* elements in a single-dimensional structure.
- The elements are added and removed in FIFO format.
- When elements are removed from the queue, the operation is called `dequeue`, when elements are added to the queue, the operation is called `enqueue`.

![queue_operations][queue_operations]

### Tree
- In the context of algorithms, a tree is one of the most useful data structures due to its hierarchical nature data storage capabilities.
- While designing algorithms, we use trees wherever we need to represent hierarchical relationships among the data elements that we need to store or process.
- Each tree has a finite set of nodes so that it has a starting data element called a *root* and a set of nodes joined together by linked called *branches*.
- Terminology

| Elements              | Description                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Root node             | A node with no parent is called the `root` node. In algorithms, the root node holds the most important value in the tree structure                 |
| Level of a node       | The distance from the root node is the level of a node                                                                                             |
| Siblings nodes        | Two nodes in a tree are called *siblings* if they are at the same level                                                                            |
| Child and parent node | A node F is a child of node C, if both are directly connected and the level of node C is less than node F                                          |
| Degree of a node      | The degree of a node is the number of children it has                                                                                              |
| Degree of a tree      | The degree of a tree is equal to the maximum degree that can be found among the constituent nodes of a tree                                        |
| Subtree               | A subtree of a tree is a portion of the tree with the chosen node as the root node of the subtree and all of the children as the nodes of the tree |
| Leaf node             | A node in a tree with no children is called a *leaf* node                                                                                          |
| Internal node         | Any mode that is neither a root nor a leaf node is an internal node. An internal node will have at least one parent and at least on child node     |

- Types of trees
  - **Binary tree**: If the degree of a tree is two, that tree is called a *binary tree*.
  ![bin_tree][bin_tree]
  - **Full tree**: A full tree is the one in which all of the nodes are of the same degree, which will be equal to the degree of the tree.
  ![full_tree][full_tree]
  - **Perfect tree**: A perfect tree is a special type of full tree in which all the leaf nodes are at the same level.
  - **Ordered tree**: If the children of a node are organized in some order according to particular criteria, the tree is called an *ordered tree*.

[stack_operations]: ../_resources/images/stack_operations.png
[queue_operations]: ../_resources/images/queue_operations.png
[bin_tree]: ../_resources/images/bin_tree.png
[full_tree]: ../_resources/images/full_tree.png