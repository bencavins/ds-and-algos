m = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['x', 'y', 'z'],
]

for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        print(f'i=={i}, j=={j}, m[i][j]=={m[i][j]}')