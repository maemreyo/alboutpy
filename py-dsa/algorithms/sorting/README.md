# Sorting algorithms
- In the era of big data, the ability to efficiently sort items in a complex data structure is quite important as it is needed by many modern algorithms.
- The right strategy to sort data will depend on the size and type of the data.

## Bubble Sort
- Bubble sort is the simplest and slowest algorithm used for sorting.
- It is designed in a way that the highest value in its list bubbles its way to the top as the algorithm loops through iterations.
- As its worst-case performance is `O(N2)`, it should be used for smaller datasets.

### The logic behind the scene
- Bubble sort is based on various iterations, called **passes**. For the list size `N`, bubble sort will have `N - 1` passes.
- Bubble sort compares adjacent neighbors values. If the value at a higher position is higher in value than the value at a lower position, we exchange the values. This iteration continues until we reach the end of the list.
![first_pass_bubble_sort.png](_resources/images/first_pass_bubble_sort.png)
- Implementation: [Bubble Sort](bubble.py)

### Performance Analysis
- It is easier to see that bubble sort involves two levels of loops:
  - **An outer loop**: This is also called **passes**.
  - **An inner loop**: This is when the remaining unsorted elements in the list are sorted, until the highest value is bubbled to the right. The first pass will have `N-1` comparisons, the second pass will have `N-2` comparisons, and each subsequent pass will reduce the number of comparisons by one.
- Due to two levels of looping, the worst-case runtime complexity would be `O(N2)`.