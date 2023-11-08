def print_mat(m):
    for row in m:
        print(row)

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# one way of looping (no indices)
# for row in mat:
#     for cell in row:
#         print(cell)

# # loop with indices
# for i in range(0, len(mat)):
#     row = mat[i]
#     for j in range(0, len(row)):
#         print(mat[i][j])