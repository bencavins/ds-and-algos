# time complexity O(n) aka linear
# space complexity O(1)
def has_char(s, c):
    for character in s:
        if character == c:
            return True
    return False


# has_char('a'*10, 'a')  # 10
# has_char('a'*100, 'z')  # 100
# has_char('a'*1000, 'z')  # 1000



# O(n * m) ~ O(n^2)
def char_search(array, c):
    ops = 0
    for string in array:
        has_char(string, c)  # O(n)
    print(f'n: {len(array)}, ops: {ops}')
    return False


# O(n^2) quadratic time
def sum_matrix(m):
    total = 0
    for row in m:
        for item in row:
            total += item
    return total

# O(1) aka constant time
def exclaim(s):
    return s + '!'


# time complexity -- O(n^2)
# space complexity -- O(n)
def double(array):
    result = []
    for item in array:
        result.insert(0, item * 2)  # O(n)
    return result



# O(n), linear search
def search(array, number):
    for num in array:
        if num == number:
            return True
    return False


# O(log n), very efficient 
def binary_search(l, target):
    left_i = 0
    right_i = len(l) - 1

    while left_i <= right_i:
        mid_i = (left_i + right_i) // 2

        if l[mid_i] == target:
            return mid_i
        elif l[mid_i] < target:
            left_i = mid_i + 1
        else:
            right_i = mid_i - 1
    
    return -1
