ans = ''
names = [0 for i in range(26)]
for i in range(int(input())):
    name = input()
    idx = ord(name[0]) - 97
    names[idx] += 1

for i in range(len(names)):
    if names[i] >= 5:
        ans += chr(i + 97)

if ans == '':
    print("PREDAJA")
else:
    print(ans)