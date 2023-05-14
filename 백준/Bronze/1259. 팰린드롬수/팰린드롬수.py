n = input()
while n != '0':
    half = len(n) // 2
    first, second = '', ''
    if len(n) % 2 == 1:
        first, second = n[:half], n[half+1:][::-1]
    else:
        first, second = n[:half], n[half:][::-1]

    if first == second:
        print('yes')
    else:
        print('no')

    n = input()