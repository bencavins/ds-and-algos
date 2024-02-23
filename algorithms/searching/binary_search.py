"""
Given a list l and a target, return the index of the target
if it exists, -1 otherwise.

Use binary search.

What is the runtime complexity?
"""

# O(log n)
def binary_search(l, target):
    left_i = 0 
    right_i = len(l) - 1

    while left_i <= right_i:
        mid_i = (left_i + right_i) // 2
        print(left_i, mid_i, right_i)

        if l[mid_i] == target:
            return mid_i
        elif l[mid_i] < target:
            left_i = mid_i + 1
        else: # l[mid_i] > target
            right_i = mid_i - 1
    
    return -1



if __name__ == '__main__':
    # test 1
    l = [0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 7, 8]
    res = binary_search(l, 3)
    assert res == 9

    # test 2
    l = ['a', 'b', 'c', 'd', 'e', 'f']
    res = binary_search(l, 'x')
    assert res == -1

    # test 3
    l = []
    res = binary_search(l, 7)
    assert res == -1