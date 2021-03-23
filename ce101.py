'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

from csv import DictReader


def find_user(first, last):
    with open('users.csv') as fo:
        csv_dictreader = DictReader(fo)
        row_counter = 0
        for row in csv_dictreader:
            row_counter += 1
            if row['First Name'] == first and row['Last Name'] == last:
                return row_counter
        return '{} {} not found.'.format(first, last)


print(find_user("Alan", "Turing"))
print(find_user('Colte', 'Steele'))
print(find_user("Alan", "Turing"))
