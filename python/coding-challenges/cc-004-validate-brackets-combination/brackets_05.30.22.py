'''
"()" 
"()[]{}"
"(]"
"([)]"
"{[]}"
'''
def match(string):
    history = [] # stack variable ['(']
    open_brackets = ['(','[','{']
    close_brackets = [')',']','}']
    for letter in string:
        if letter in open_brackets:
            history.append(letter)
        elif letter in close_brackets:
            if len(history) > 0:
                bracket_type = close_brackets.index(letter)
                if (open_brackets[bracket_type]) == history[-1]:
                    history.pop()
                else:
                    return False
            else:
                return False
    if len(history) == 0:
        return True
    return False




print(match("()"))
print(match("()[]{}"))
print(match("(]"))
print(match("([)]"))
print(match("{[]}"))
print(match(""))
print(match("("))
print(match(")"))