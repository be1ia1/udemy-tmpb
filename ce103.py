from csv import DictReader, DictWriter


def delete_users(first, last):
    with open('users.csv') as fo:
        csv_reader = DictReader(fo)
        user_d_count = 0
        data = []
        for row in csv_reader:
            if row['First Name'] == first and row['Last Name'] == last:
                user_d_count += 1
            else:
                data.append(row)
    with open('users.csv', 'w', newline='') as fo:
        fieldnames = ['First Name', 'Last Name']
        csv_writer = DictWriter(fo, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)
    return 'Users deleted: {}'.format(user_d_count)


print(delete_users("Colt", "Steele"))
