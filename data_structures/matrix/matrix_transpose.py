m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# O(n^2)
# O(n^2)
def transpose(m):
    res = []
    for j in range(0, len(m[0])):
        row = []
        for i in range(0, len(m)):
            row.append(m[i][j])
        res.append(row)

    return res


def print_mat(m):
    for row in m:
        print(row)