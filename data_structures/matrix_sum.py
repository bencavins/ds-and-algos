m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# time == O(N*M)
# space == O(1)
def mat_sum(m):
    count = 0
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            count += m[i][j]
    return count