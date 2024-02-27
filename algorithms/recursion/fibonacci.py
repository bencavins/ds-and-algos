# 0 1 1 2 3 5 8 13 21...


# cache

# {n: fib(n)}
cache = {}

def fib(n):
    # check cache for this value
    if n in cache:
        print('cache hit')
        return cache[n]
    
    if n < 0:
        return None

    if n == 0:
        return 0
    if n == 1:
        return 1
    prev = fib(n - 1)
    cache[n-1] = prev  # add this value to cache
    prev_prev = fib(n - 2)
    cache[n-2] = prev_prev # same here
    return prev + prev_prev



print(fib(10))