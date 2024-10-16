def mat_eq(m1, m2):
    """Should return True if m1 and m2 are equal"""
    pass


if __name__ == '__main__':
    assert mat_eq([[]], [[]])

    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert mat_eq(m1, m2)

    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    m2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    assert not mat_eq(m1, m2)