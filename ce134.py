'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''

from functools import wraps

def add(a, b):
    return a + b

def once(func):
    @wraps(func)
    def inner(*args, **kwargs):
        inner.calls += 1
        return func(*args, **kwargs)
    inner.calls = 0
    return inner

oneAddition = once(add)
print(oneAddition(2, 2))
print(oneAddition(2, 2))
print(oneAddition.calls)
