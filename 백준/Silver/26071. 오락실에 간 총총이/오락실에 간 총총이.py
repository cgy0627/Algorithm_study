n = int(input())

gomx = []
gomy = []

for y in range(n):
    for x, char in enumerate(input()):
        if char == 'G':
            gomx.append(x)
            gomy.append(y)

left = max(gomx) - 0
right = n-1 - min(gomx)
no_x = 0 if len(set(gomx)) == 1 else 1501
# print(gomx)
# print(left, right, no_x)

top = max(gomy) - 0
bottom = n-1 - min(gomy)
no_y = 0 if len(set(gomy)) == 1 else 1501
# print(gomy)
# print(top, bottom, no_y)

print(min(left, right, no_x) + min(top, bottom, no_y))