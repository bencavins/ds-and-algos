# time: O(n) linear
# space: O(1) constant
def sum(numbers):
    total = 0
    op_count = 0
    for num in numbers:
        total += num
        op_count += 2
    print(f'op_count == {op_count}')
    return total

# sum([1, 2, 3])
# sum([1, 2, 3, 4, 5, 6, 7, 8, 9])
# sum([1] * 100)


# time: O(n) linear
# space: O(1) constanct
def search(nums, target):
    for num in nums:
        if num == target:
            return True
    return False


search([1, 2, 3, 4, 5], 3)


# time: O(1) constant
# space: O(1) constant
def get_first(nums):
    return nums[0]

# get_first([1])
# get_first([1] * 100000)

# time: O(n^2) quadratic
# space: O(n) linear
def get_unique(nums):
    unique = []
    for num in nums:
        if num not in unique:
        # if not search(unique, num):  # O(n)
            unique.append(num) # O(1)
    return unique

