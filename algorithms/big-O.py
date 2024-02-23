"""
O(1) == constant time



# best case
# avg case
# worst case

"""

# O(n)
def linear(n):
    ops = 0
    for x in range(n):
        ops += 1
    print(f'n={n} ops={ops}')


# O(n^2)
def quadratic(n):
    ops = 0
    for x in range(n):
        for y in range(n):
            ops += 1
    print(f'n={n} ops={ops}')

# # O(n^3)
# def quadratic(n):
#     ops = 0
#     for x in range(n):
#         for y in range(n):
#             for z in range(n):
#                 ops += 1
#     print(f'n={n} ops={ops}')


# O(n^2)
def f(n):
    x = 1 + 1
    quadratic(n) # O(n^2)
    return x



# O(n^2)
def search(n):
    order(n)  # O(n^2)
    search(n): # O(log(n))


quadratic(10)
quadratic(100)
quadratic(1000)