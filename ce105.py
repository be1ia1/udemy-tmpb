# don't forget to import re

# define parse_bytes below:

import re


def parse_bytes(string):
    pattern = re.compile(r'\b[01]{8}\b')
    match = re.findall(pattern, string)
    return match

print(parse_bytes('dfgd1010101010101gdfg 456456897 534534'))
print(parse_bytes('dsfgdsgd gdgdgd'))