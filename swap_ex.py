import re

titles = ['Tales of Mopria (1976)', 'Lake of Fear (1099)']

pattern = re.compile(r'([\w ]+) \((\d{4})\)')

for i in titles:
    answer = pattern.sub('\g<2> - \g<1>', i)
    print(answer)