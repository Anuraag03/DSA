def balancedBrackets(s):
    stack = []
    for i in s:
        if i in '({[':
            stack.append(i)
        else:
            if not stack:
                return False
            top = stack.pop()
            if i == ')' and top!='(':
                return False
            elif i =='}' and top!='{':
                return False
            elif i==']' and top!='[':
                return False
    return len(stack)==0 
print(balancedBrackets('({{}})'))
print(balancedBrackets('{}[()'))