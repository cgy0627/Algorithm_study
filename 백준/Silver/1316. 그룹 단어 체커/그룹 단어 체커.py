n = int(input())
ans = 0
for i in range(n):
    word = input()
    temp = ['']
    group_word = True
    for char in word:
        if (char in temp) & (temp[-1] != char):
            group_word = False
            break
        else:
            temp.append(char)
    if group_word:
        ans += 1

print(ans)