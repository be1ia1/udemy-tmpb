'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''


def is_odd_string(string):
    alphabet = [chr(char) for char in range(97, 123)]
    alphabet.insert(0, None)
    return sum([alphabet.index(letter) for letter in string]) % 2 == 1


print(is_odd_string('a'))
print(is_odd_string('aaaa'))
print(is_odd_string('amazing'))
print(is_odd_string('veryfun'))
print(is_odd_string('veryfunny'))
