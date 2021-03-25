'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''


def valid_parentheses(string):
    if (string.startswith(')') or string.endswith('(')):
        return False
    return True


print(valid_parentheses("()")) # True 
print(valid_parentheses(")(()))")) # False 
print(valid_parentheses("(")) # False 
print(valid_parentheses("(())((()())())")) # True 
print(valid_parentheses('))((')) # False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False