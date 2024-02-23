

# time: O(n^2)
# space: O(1)
def find_mode_v1(l):
    max_item, max_count = None, 0

    for item in l:
        count = 0
        for x in l:
            if item == x:
                count += 1
        if count > max_count:
            max_item, max_count = item, count
    
    print(max_item, max_count)
    return max_item


# time: O(n)
# space: O(n)
def find_mode(l):
    d = {}

    for item in l:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    
    print(d)
    max_item, max_count = None, 0
    for key in d:
        if d[key] > max_count:
            max_item, max_count = key, d[key]
    return max_item


if __name__ == '__main__':
    l = [1, 2, 3, 3, 3, 4, 5, 3, 4, 1, 8, 3, 3, 3, 3, 3, 3]
    assert find_mode(l) == 3