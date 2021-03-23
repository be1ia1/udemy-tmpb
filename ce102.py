'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

from csv import DictReader, DictWriter


def update_users(oldf, oldl, newf, newl):
    with open('users.csv') as fo:
        csv_dictr = DictReader(fo)
        data = []
        users_ucount = 0
        for row in csv_dictr:
            if row['First Name'] == oldf and row['Last Name'] == oldl:
                data.append({'First Name': newf, 'Last Name': newl})
                users_ucount += 1
            else:
                data.append(row)
    with open('users.csv', 'w', newline='') as fo:
        fieldnames = ['First Name', 'Last Name']
        csv_dictw = DictWriter(fo, fieldnames=fieldnames)
        csv_dictw.writeheader()
        csv_dictw.writerows(data)
    return 'Users updated: {}.'.format(users_ucount)


print(update_users("Grace", "Hopper", "Hello", "World"))
