def transpose(m):
    """Should transpose matrix m"""
    pass


if __name__ == '__main__':
    input_m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    assert transpose(input_m) == expected