import re


def censor(string):
    pattern = re.compile(r'frack\b|frack[a-z]+', re.I)
    answer = pattern.sub("CENSORED", string)
    return answer

print(censor('Frack you'))
print(censor('I hope you fracking die'))
print(censor('you fracking Frack'))