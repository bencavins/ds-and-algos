# ds-and-algos

## Algorithms

### Big-O Notation

[Intro to Big-O](https://dev.to/sarah_chima/the-big-o-notation-an-introduction-34f7)

![big-o graph](https://res.cloudinary.com/practicaldev/image/fetch/s--JlhrS_jk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://thepracticaldev.s3.amazonaws.com/i/r38ytuycnzi6hd8dnevh.png)

### Search Algorithms

[Info on Search Algorithms](https://www.geeksforgeeks.org/searching-algorithms/)

#### Sequential Search

[linear_search.py](./algorithms/searching/linear_search.py)

Check every item in the list to see if the target exists.

Pros:
- simple
- works with unordered lists

Cons:
- Can be slow if list is large

[Info on Sequential Search](https://www.geeksforgeeks.org/linear-search/)

#### Binary Search

[binary_search.py](./algorithms/searching/binary_search.py)

Requries the list to be sorted.

Continually check the middle element of a list. If the target is greater than the middle
element, disregard everything to the left and repeat the process on the right sub-list. If 
the target is less than the middle element, disregard everything to the right and repeat the
process on the left sub-list. Continue until the target is found or the search space is exhausted.

[Info on Binary Search](https://www.geeksforgeeks.org/binary-search/)

##### Binary Search vs Sequential Search

![animation](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif)

##### Practice Problems

- [Find the largest 3 elements](https://www.geeksforgeeks.org/find-the-largest-three-elements-in-an-array/)
- [Find the missing number](https://www.geeksforgeeks.org/find-the-missing-number/)

### Sorting

[List of sorting algorithms](https://www.geeksforgeeks.org/sorting-algorithms/)

### Recursion

## Data Structures

### Matrix

[matrix.py](./data_structures/matrix.py)

### Linked List
[linked_list.py](./data_structures/linked_list.py)

### Stack
[stack.py](./data_structures/stack.py)

### Queue
[queue.py](./data_structures/queue.py)

### Tree
[tree.py](./data_structures/tree.py)