# time == O(n^2)
# space == O(n^2)
def identity(n):
    mat = []
    
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        mat.append(row)
    
    return mat


def print_mat(m):
    for row in m:
        print(row)
