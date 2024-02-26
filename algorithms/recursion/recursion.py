def f(n):
    if n <= 0:  # base case
        return  # not loop (no recursive call)
    else:
        print(f'before, n == {n}')
        f(n - 1)  # loop (recursive call) (code pauses here)
        print(f'after, n == {n}')
        return 


f(10)
print('done')