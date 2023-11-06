# time complexity

# time complexity == O(1)
# space complexity == O(1)
def f1(n):
    count = 0

    1+1  # one op
    count += 1

    print(n)  # one op
    count += 1

    return count

# time == O(n)
# space == O(1)
def f2(n):
    count = 0

    for x in range(n):
        print(x)  # one op
        count += 1

    return count

# O(n^2)
def f3(n):
    count = 0

    # O(n^2)
    for x in range(n):
        for y in range(n):
            x * y  # one op
            count += 1
    
    return count


print(f'f3(1) == {f3(1)}')
print(f'f3(10) == {f3(10)}')
print(f'f3(100) == {f3(100)}')

