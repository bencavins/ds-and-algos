# time == O(n*m)
# space == O(1)
def mat_eq(m1, m2):
    """Should return True if m1 and m2 are equal"""
    if len(m1) != len(m2):
        return False

    for i in range(0, len(m1)):
        if len(m1[i]) != len(m2[i]):
            return False
        for j in range(0, len(m1[i])):
            if m1[i][j] != m2[i][j]:
                return False
    return True


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
        [1, 2, 3],
        [4, 5, 6],
        [7, 8]
    ]
    assert not mat_eq(m1, m2)