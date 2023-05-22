letters = set(input())
mobis = {'M', 'O', 'B', 'I', 'S'}

ans = mobis - letters

print('YES' if not ans else 'NO')