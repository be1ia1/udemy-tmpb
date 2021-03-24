'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''
# кількість разів за числом слідує більше число

def find_greater_numbers(list1):
    great_counter = 0
    last_el = len(list1) - 1
    while list1[:last_el]:
        great_counter += sum([list1[last_el] > el for el in list1[:last_el]])
        last_el -= 1
    return great_counter


print(find_greater_numbers([6,1,2,7]))
print(find_greater_numbers([5,4,3,2,1]))