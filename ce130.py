'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

# sum three - odd


def three_odd_numbers(lst):
    answers = []
    first_el = 0
    last_el = 3
    while last_el <= len(lst):
        answers.append(sum(lst[first_el:last_el]) % 2)
        first_el += 1
        last_el += 1
    return any(answers)


print(three_odd_numbers([1,2,3,4,5]))
