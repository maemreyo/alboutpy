# Searching Algorithms
- Efficiently searching data in complex data structures is one of the most important functionalities.
- The simplest approach, which will not be that efficient, is to search for the required data in each data point.
- But, as the data becomes bigger in size, we need more sophisticated algorithms designed to for searching data.

## Linear Search
- The simplest strategy for searching data is to simply loop through each element looking for the target. Each data point is searched for a match and when a match is found, the results are returned and the algorithm exits.
- Otherwise, the algorithm keeps on searching until it reaches the end of the data. The obvious disadvantage of linear search is that it is very slow due to the inherent exhaustive search.
- The advantage is that the data does not need to be sorted.
- Implementation: [Linear Search](linear.py)

### Performance Analysis
- Linear search is a simple algorithm that performs an exhaustive search. Its worst-case behavior is `O(N)`.

## Binary Search
- The pre-requisite of the binary search algorithm is sorted data. The algorithm iteratively divides a list into two parts and keeps a track of the lowest and highest indices until it finds the value it is looking for.
- Implementation: [Binary Search](binary.py)