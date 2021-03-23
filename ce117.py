'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''


def truncate(stri, num):
    if num < 3:
        return "Truncation must be at least 3 characters."
    elif num > len(stri):
        return stri
    return '{}...'.format(stri[:num - 3])


print(truncate("Super cool", 2))
print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
