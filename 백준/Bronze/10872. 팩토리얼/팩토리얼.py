N = int(input())
a,b = 1,1
for i in range(2,N+2):
    a,b = a*b, i

print(a)