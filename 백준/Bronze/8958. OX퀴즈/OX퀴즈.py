# 8958 OX퀴즈

N = int(input())
for i in range(N):
    ox = input()
    
    acc = 0
    total = 0
    for char in ox:
        if char == "X":
            acc = 0
        elif char == "O":
            acc += 1
            total += acc
    print(total)