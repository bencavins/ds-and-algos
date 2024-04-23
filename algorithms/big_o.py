# RunTime Complexity
# Big-O Notation



# O(1) constant time
def get_first_thing(my_list):
    count = 0
    count += 1
    print(f"count: {count}")
    return my_list[2]

def add(x, y):
    count = 0
    count += 1
    print(f"count: {count}")
    return x + y


# O(n)  linear time 
def is_in(my_list, target_value):
    count = 0
    for item in my_list:
        count += 1
        if item == target_value:
            return True
    
    print(f'n: {len(my_list)} count: {count}')
    return False


# O(n^2)
def func(my_list):
    count = 0
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            count += 1
    print(f'n: {len(my_list)} count: {count}')


func([1]*10)
func([1]*100)
func([1]*1000)