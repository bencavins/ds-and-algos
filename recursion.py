# def f(n):
#     if n == 0:
#         print('base case')
#         return
#     else:
#         print(f'inside function f({n})')
#         f(n-1)


# f(10)


# factorial 5! == 1*2*3*4*5
def factorial_no_recursion(n):
    prod = 1
    for x in range(1, n+1):
        prod *= x
    return prod

def factorial(n):  # (with recursion)
    if n == 1:
        print('base case, returning 1')
        return 1
    else:
        print(f'computing f({n-1})')
        result = factorial(n-1)
        print(f'returning f({n-1}) * {n} == ({result * n})')
        return result * n

# fibonacci sequence   0 1 1 2 3 5 8 13...
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)