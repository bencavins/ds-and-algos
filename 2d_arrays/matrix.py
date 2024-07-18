# row-ordered (first index is the row)
# usually rectangular (not always)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]
]


# O(n*m)  (n and m are width and height)
def traverse(mat):
    for row in mat:
        for cell in row:
            print(cell)

def traverse_with_index(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j])

# traverse(matrix)
traverse_with_index(matrix)
# print(len(matrix))