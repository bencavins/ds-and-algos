"""
Given a list l and a target, return the index of the target
if it exists, -1 otherwise.

Use binary search.

What is the runtime complexity?
"""

def binary_search(l, target):
    pass


if __name__ == '__main__':
    # test 1
    l = [1, 5, 2, 0, 0, 3, 7, 4, 8]
    res = binary_search(l, 3)
    assert res == 6

    # test 2
    l = ['a', 'b', 'c', 'd', 'e', 'f']
    res = binary_search(l, 'x')
    assert res == -1

    # test 3
    l = []
    res = binary_search(l, 7)
    assert res == -1