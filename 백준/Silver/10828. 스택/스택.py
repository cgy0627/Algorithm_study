import sys

N = int(sys.stdin.readline().strip())

stack = []
for i in range(N):
    command = sys.stdin.readline().strip()

    if command.startswith("push"):
        stack.append(int(command.split()[1]))
    
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        
    elif command == "size":
        print(len(stack))
    
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])