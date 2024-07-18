
# time: O(n*m)
# space: O(1)
def mat_sum(m):
    """Should return the sum of all values in m"""
    count = 0
    for row in m:
        for value in row:
            count += value
    return count


if __name__ == '__main__':
    m = [
        [1 , 2 , 3 , 4 ],
        [5 , 6 , 7 , 8 ],
        [9 , 10, 11, 12],
        [13, 14, 15, 16],
    ]
    assert mat_sum(m) == 136

    m2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert mat_sum(m2) == 21