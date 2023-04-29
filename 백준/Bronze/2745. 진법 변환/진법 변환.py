N, B = input().split()
B = int(B)

ans = 0
for char in N:
    if char.isnumeric():
        ans = ans * B + int(char)
    else:
        ans = ans * B + ord(char) - 55

print(ans)