string = input();

res = ''
for char in string:
    if char.islower():
        res += char.upper()
    else:
        res += char.lower()

print(res)