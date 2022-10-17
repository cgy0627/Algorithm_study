import sys

while(True):
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":    # 마지막 줄
        break
    
    stack = []
    pairs = {')':'(', ']':'['}
    for char in sentence:
        if (char == '(') | (char == '['):
            stack.append(char)
        elif (char == ')') | (char == ']'):
            if len(stack) == 0:
                stack.append(char)
                break
            elif stack[-1] != pairs[char]:
                break
            elif stack[-1] == pairs[char]:
                stack.pop()
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')