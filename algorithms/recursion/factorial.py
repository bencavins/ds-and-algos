def factorial(n):
    if n == 1:  # base case
        return n
    else:
        return factorial(n - 1) * n


print(factorial(5))