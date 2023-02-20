# Searching Algorithms

- Efficiently searching data in complex data structures is one of the most important functionalities.
- The simplest approach, which will not be that efficient, is to search for the required data in each data point.
- But, as the data becomes bigger in size, we need more sophisticated algorithms designed to for searching data.

## Linear Search

- The simplest strategy for searching data is to simply loop through each element looking for the target. Each data
  point is searched for a match and when a match is found, the results are returned and the algorithm exits.
- Otherwise, the algorithm keeps on searching until it reaches the end of the data. The obvious disadvantage of linear
  search is that it is very slow due to the inherent exhaustive search.
- The advantage is that the data does not need to be sorted.
- Implementation: [Linear Search](linear.py)

### Performance Analysis

- Linear search is a simple algorithm that performs an exhaustive search. Its worst-case behavior is `O(N)`.

## Binary Search

- The pre-requisite of the binary search algorithm is sorted data. The algorithm iteratively divides a list into two
  parts and keeps a track of the lowest and highest indices until it finds the value it is looking for.
- Implementation: [Binary Search](binary.py)

### Performance Analysis

- Binary search is so named because at each iteration, the algorithm bifurcates the data into two parts. If the data has
  _N_ items, it will take a maximum of _O(logN)_ steps to iterate. This means that the algorithm has an _O(logN)_
  runtime.

## Interpolation Search

- Interpolation search is more sophisticated than binary search. It uses the target value to estimate the position of
  the element in the sorted array.
- Assume we want to search for a word in an English dictionary, such as the word _river_. We will use this information
  to interpolate and start searching for words starting with _r_.
- Implementation: [Interpolation Search](interpolation.py)

### Performance Analysis

- If the data is unevenly distributed, the performance of the interpolation search algorithm will be poor.
- The worst-case performance of this algorithm is `O(N)` and if the data is somewhat reasonably uniform, the best
  performance is `O(log(logN))`.