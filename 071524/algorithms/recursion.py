# O(n)
def countdown(n):
    """Counts down from n"""
    if n == 0:
        print('blastoff')
        return

    print(n)
    countdown(n-1)


# O(n)
def factorial(n):
    """Returns n!"""
    if n == 1:
        return n
    else:
        print(f'computing {n-1}')
        x = factorial(n-1) * n
        print(f'fact({n}) == {x}')
        return x

# print(factorial(5))


# 0 1 1 2 3 5 8 13...
# O(2^n)
cache = {}
def fibonacci(n):
    """Returns the nth fibonacci number"""
    # check the cache 
    if n in cache:
        print('cache hit!')
        return cache[n]
    else:
        print('cache miss :(')

    # run my function
    if n == 0:
        return 0
    if n == 1:
        return 1
    x = fibonacci(n-1)
    cache[n-1] = x
    y = fibonacci(n-2)
    cache[n-2] = y
    return x + y

# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))
