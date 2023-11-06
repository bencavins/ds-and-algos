# time  == O(n)
# space == O(1)
def in_place_rev(l):
    mid = len(l) // 2
    for i in range(0, mid):
        tmp = l[i]
        l[i] = l[len(l) - 1 - i]
        l[len(l) - 1 - i] = tmp
    return l

# time  == O(n)
# space == O(n)
def rev(s):
    end_idx = len(s) - 1  # O(1)
    new_str = "" # O(1)

    for i in range(end_idx, -1, -1):  # O(1)
        new_str += s[i]
    
    return new_str

print(rev(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
print(in_place_rev(['a', 'b', 'c', 'd', 'e', 'f', 'g']))