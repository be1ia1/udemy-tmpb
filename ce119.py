'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''


def range_in_list(lst, start=0, end=None):
    if not end:
        return sum(lst[start:])
    return sum(lst[start:end + 1])


print(range_in_list([1, 2, 3, 4], 0, 2))
print(range_in_list([1, 2, 3, 4], 0, 3))
print(range_in_list([1, 2, 3, 4], 1))
print(range_in_list([1, 2, 3, 4]))
print(range_in_list([1, 2, 3, 4], 0, 100))
print(range_in_list([], 0, 1))
