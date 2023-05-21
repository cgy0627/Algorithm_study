from collections import deque

T = int(input())
for i in range(T):
    command = input()
    n = int(input())
    lst = input().replace('[', '').replace(']', '')
    lst = [] if lst == '' else deque(map(int, lst.split(',')))

    end = 1
    for char in command:
        if char == 'R':
            end = 0 if end else 1
        else:
            if len(lst) < 1:
                lst = 'error'
                break
            if end:
                lst.popleft()
            else:
                lst.pop()

    if lst == 'error':
        print(lst)
    else:
        if not end:
            lst.reverse()
        print(str(list(lst)).replace(' ', ''))