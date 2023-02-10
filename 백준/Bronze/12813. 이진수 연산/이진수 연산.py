A = int(input(), 2)
B = int(input(), 2)
n = 100000
mask = 2 ** n - 1

print(bin(A & B)[2:].zfill(n))
print(bin(A | B)[2:].zfill(n))
print(bin(A ^ B)[2:].zfill(n))
print(bin(A^mask)[2:].zfill(n))
print(bin(B^mask)[2:].zfill(n))