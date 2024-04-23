def countdown(n):
    # base case
    if n == 0:
        print('launch!')
        return
    else:
        print(n)
        countdown(n-1)  # recursive call
        # print(f'returning from coundown({n})')
        return


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


# 0 1 1 2 3 5 8 13...

cache = {}
def fib(n):
    if n in cache:
        print('cache hit')
        return cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    x = fib(n-1)
    cache[n-1] = x
    y = fib(n-2)
    cache[n-2] = y
    return x + y


print(fib(100))
print(cache)