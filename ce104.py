import re


def is_valid_time(time):
    pattern = re.compile(r'(\d{1}|\d{2})\:(\d{1}|\d{2})')
    match = re.fullmatch(pattern, time)
    return True if match else False

print(is_valid_time('10.00'))