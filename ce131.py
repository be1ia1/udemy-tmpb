'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

# define mode below:


def mode(lst):
    answer, count = None, 0
    for i in lst:
        if count < lst.count(i):
            answer = i
            count = lst.count(i)
    return answer

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))