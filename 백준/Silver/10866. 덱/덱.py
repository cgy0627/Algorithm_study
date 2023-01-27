from collections import deque
import sys

n = int(sys.stdin.readline())

ans = deque([])

for i in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == "push_front":
        ans.appendleft(command[1])
    elif command[0] == "push_back":
        ans.append(command[1])
    elif command[0] == "pop_front":
        if ans:
            print(ans.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if ans:
            print(ans.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(ans))
    elif command[0] == "empty":
        if ans:
            print(0)
        else:
            print(1)
    else:
        if ans:
            if command[0] == "front":
                print(ans[0])
            elif command[0] == "back":
                print(ans[-1])
        else:
            print(-1)