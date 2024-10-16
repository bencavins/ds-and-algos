# In-place rotate it by 90 degrees in a clockwise direction
def rotate(m):
    """Should rotate the matrix m 90 degress clockwise"""
    pass

 
if __name__ == '__main__':
 
    mat = [
        [1 , 2 , 3 , 4],
        [5 , 6 , 7 , 8],
        [9 , 10, 11, 12],
        [13, 14, 15, 16]
    ]
    expected = [
        [13, 9 , 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]
    assert rotate(mat) == expected