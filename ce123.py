'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]

sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

sum_up_diagonals(list2) # 30

list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]

sum_up_diagonals(list4) # 68
'''


def sum_up_diagonals(list1):
    answer = []
    start_left = 0
    start_right = len(list1) - 1
    for lst in list1:
        answer.append(lst[start_left])
        start_left += 1
        answer.append(lst[start_right])
        start_right -= 1
    return sum(answer)


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]

print(sum_up_diagonals(list1))
print(sum_up_diagonals(list2))
print(sum_up_diagonals(list3))
print(sum_up_diagonals(list4))