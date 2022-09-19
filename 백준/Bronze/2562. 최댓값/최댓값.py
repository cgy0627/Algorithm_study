# 2562 최댓값

maxNum = 0
index = 0
for i in range(9):
    num = int(input())
    
    if num > maxNum:
        maxNum = num
        index = i + 1

print(f'{maxNum}\n{index}')