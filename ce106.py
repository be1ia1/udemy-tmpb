import re

def parse_date(string):
    pattern = re.compile(r'(?P<d>\b[0-9]{2})[/,.]{1}(?P<m>[0-9]{2})[/,.]{1}(?P<y>[0-9]{4})\b')
    match = re.search(pattern, string)
    answer = {}
    if match:
        answer['d'] = match.group('d')
        answer['m'] = match.group('m')
        answer['y'] = match.group('y')
        if int(answer['d']) < 32 and int(answer['m']) < 13:
            return answer
print(parse_date('22.13.9811'))