## Sorting algorithms 

#### Requirements:
```
pip install matplotlib
```

Input: A list with 1000 distinct numbers in the range of 1-1000.

Output: A sorted list and the time the sorting algorithm used.

### Bubble sort
A terrible sorting algorithm. 
Worst case: O(n^2)
Best case: O(n) if sorted
Average case: O(n^2) 

#### How does it work 
Iterate through the whole list:
Compare adjacent elements, if the right one is bigger, swap.
Repeat until no swaps are made.

1, 5, 6, 7, 2, 4

->1, 5, 6, 7, 2, 4 

->1, 5, 6, 2, 7, 4

->1, 5, 2, 6, 7, 4

->1, 2, 5, 6, 7, 4

->1, 2, 5, 6, 4, 7

->1, 2, 5, 4, 6, 7

->1, 2, 4, 5, 6, 7

### Insertion sort
In place, Stable, easy to implement
Worst case: O(n^2)
Best case: O(n) with O(1) swaps
Average case: O(n^2) 

Even though it looks just as bad as bubble sort, it is way better in reality. (As seen in the example under)

#### How does it work
Iterate through the list, if the next item is lesser than the current item:
Find the right position in the list backwards.

1, 5, 6, 7, 2, 4

-> 1, 2, 5, 6, 7, 4

-> 1, 2, 4, 5, 6, 7


### Merge sort
Divide and conquer algorithm. Running time O(nlogn)
#### How does it work
The idea is to split the lists in half until all the lists are of size 1.
When the the lists are split into lists with size one, start merging the lists. 

Splitting
1, 5, 6, 7, 2, 4,

-> 1,5, 6 and 7,2,4

-> 1,5 and 6 and 7,2 and 4

1 and 5 and 6 and 7 and 2 and 4

merge part:

1,5 and 6,7 and 2,4

1,5,6,7 and 2,4,7

1,2,4,5,6,7


### Quicksort
Divide and conquer algorithm
WC O(n^2) -> pivot is largest or smallest value in list
AC O(nlogn)
BC O(nlogn)

