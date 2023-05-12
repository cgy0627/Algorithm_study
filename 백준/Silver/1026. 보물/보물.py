n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sort = sorted(A, reverse=True)
B_sort = sorted(B)

print(sum(A_sort[i] * B_sort[i] for i in range(len(A))))