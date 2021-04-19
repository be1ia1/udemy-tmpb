'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''


def find_the_duplicate(lst):
    doubles = [i for i in lst if lst.count(i) == 2]
    return doubles[0] if doubles else None


print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
print(find_the_duplicate([2, 1, 3, 4]))
