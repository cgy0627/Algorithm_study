n = int(input())
word = list(input())
for i in range(n-1):
    next = input()
    for j in range(len(word)):
        if word[j] != '?' and word[j] != next[j]:
            word[j] = '?'

print(''.join(word))