"""
Given a list l and a target, return the index of the target
if it exists, -1 otherwise.

Use a sequential search (aka linear search).

What is the runtime complexity?
"""

def linear_search(array, number):
    for num in array:
        if num == number:
            return True
    return False


if __name__ == '__main__':
    # test 1
    l = [1, 5, 2, 0, 0, 3, 7, 4, 8]
    res = linear_search(l, 3)
    assert res == 6

    # test 2
    l = ['a', 'b', 'c', 'd', 'e', 'f']
    res = linear_search(l, 'x')
    assert res == -1

    # test 3
    l = []
    res = linear_search(l, 7)
    assert res == -1