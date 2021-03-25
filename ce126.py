'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''


def two_oldest_ages(lst):
    answer = []
    for i in range(2):
        max_in_lst = max(lst)
        answer.insert(0, max_in_lst)
        lst.remove(max_in_lst)
    return answer


print(two_oldest_ages([1, 2, 10, 8]))
print(two_oldest_ages([6,1,9,10,4]))
print(two_oldest_ages([4,25,3,20,19,5]))
