# 3052 나머지

remainders = []

for i in range(10):
    num = int(input())
    rem = num % 42
    
    if rem not in remainders:
        remainders.append(rem)

print(len(remainders))