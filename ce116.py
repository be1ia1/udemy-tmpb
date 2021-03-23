def repeat(stri, num):
    answer = ''
    for i in range(num):
        answer += stri
    return answer


print(repeat('abc', 2))
