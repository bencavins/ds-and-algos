def factorial_old(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product


def factorial(n):
    if n == 1:  # base case
        return 1
    else:
        return n * factorial(n-1)  # recursive loop


# 0 1 1 2 3 5 8 13...

cache = {}

def fib(i):
    # check the cache for this value
    if i in cache:  # cache hit
        # print('cache hit!')
        return cache[i]

    if i == 0:  # base case
        return 0
    if i == 1:  # base case
        return 1
    
    x = fib(i-1)
    cache[i-1] = x  # add to cache
    y = fib(i-2)
    cache[i-2] = y  # add to cache
    return x + y


print(fib(500))
# print(cache)