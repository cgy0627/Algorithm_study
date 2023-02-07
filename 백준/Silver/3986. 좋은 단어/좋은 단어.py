cnt = 0
for i in range(int(input())):
    word = input()
    stack = []
    for char in word:
        if stack == []:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    if stack == []:
        cnt += 1

print(cnt)