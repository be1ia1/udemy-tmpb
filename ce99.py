from csv import writer


'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''


def add_user(first, last):
    with open('users.csv', 'a') as fo:
        csv_writer = writer(fo)
        csv_writer.writerow([first, last])


add_user("Dwayne", "Johnson")
