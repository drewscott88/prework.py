1.

def hello_name(user_name):
    print("hello_"+ user_name+"!")
hello_name("USERNAME")

2.

for num in range(1, 101, 2):
    print(num)

5.

def is_consecutive(a_list):
    if len(a_list) < 2:
        return True  # A list with 0 or 1 element is considered consecutive
    
    sorted_list = sorted(a_list)  # Sort the list in ascending order
    
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] != sorted_list[i+1] - 1:
            return False  # Non-consecutive numbers found
    
    return True  # All numbers are consecutive

list1 = [2, 3, 4, 5, 6, 7]
is_consecutive1 = is_consecutive(list1)
print(is_consecutive1)

list2 = [1, 2, 4, 5]
is_consecutive2 = is_consecutive(list2)
print(is_consecutive2)
