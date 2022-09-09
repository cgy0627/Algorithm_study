a = int(input())
b = int(input())

num = b
for i in range(len(str(b))):
    remainder = num % 10
    print(a * remainder)
    num = int(num / 10)

print(a * b)