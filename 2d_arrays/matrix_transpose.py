from matrix import print_mat

# time == O(N*M)
# space == O(N*M)
def transpose(mat):
    """Should transpose matrix m"""
    res = []
    N = len(mat)
    M = len(mat[0])

    for j in range(M):
        row = []
        for i in range(N):
            row.append(mat[i][j])
        res.append(row)

    print_mat(res)
    return res


# A novel approach (only works for number sequence)
# def transpose(mat):
#     """Should transpose matrix m"""
#     res = []
#     N = len(mat)
#     M = len(mat[0])

#     for val in mat[0]:
#         row = []
#         for x in range(N):
#             row.append((val + (M * x)) % 10)
#         res.append(row)

#     print_mat(res)
#     return res



if __name__ == '__main__':
    input_m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]
    assert transpose(input_m) == expected