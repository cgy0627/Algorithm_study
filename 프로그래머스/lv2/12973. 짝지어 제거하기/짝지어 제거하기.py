def solution(s):
    stack = []
    for char in s:
        if stack != []: # if stack is not empty
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    
    return int(stack == [])
            