original = int(input())
n = original

count = 0
while True:
    a, b = n // 10, n % 10
    new_num = a + b
    
    n = int(str(b) + str(new_num % 10))

    count += 1
    if n == original:
        break

print(count)