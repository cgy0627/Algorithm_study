A, B, V = map(int, input().split())

print((V-B)//(A-B) + ((V-B)%(A-B) > 0))