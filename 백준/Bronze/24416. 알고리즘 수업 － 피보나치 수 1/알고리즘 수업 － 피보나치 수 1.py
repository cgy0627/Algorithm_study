n = int(input())

code1 = [1] * (n+1)

for i in range(3, n+1):
    code1[i] = code1[i-1] + code1[i-2]

print(code1[n], n-3+1)