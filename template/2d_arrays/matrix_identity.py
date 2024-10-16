def mat_identity(n):
    """Should return an n x n identity matrix"""
    pass


if __name__ == '__main__':
    expected = [
        [1, 0],
        [0, 1]
    ]
    assert mat_identity(2) == expected

    expected = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    assert mat_identity(3) == expected