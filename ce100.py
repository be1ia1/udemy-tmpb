'''
print_users() # None
# prints to the console:
# Colt Steele
'''
from csv import reader


def print_users():
    with open('users.csv') as fo:
        csv_reader = reader(fo)
        next(csv_reader)
        for row in csv_reader:
            print(' '.join(row))


print_users()
