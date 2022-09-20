# 10809 알파벳 찾기

word = input()

position = {}
for i, char in enumerate(word):
    if char not in position:
        position[char] = i

for i in range(ord('a'), ord('z') + 1):
    if chr(i) in position:
        print(position[chr(i)], end = ' ')
    else:
        print(-1, end = ' ')