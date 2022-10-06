N = input()

lst = [num for num in N]
lst.sort(reverse=True)

print(''.join(lst))