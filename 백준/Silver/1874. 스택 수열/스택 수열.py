def ss(n):
    idx = 0
    ans = []
    stack = [0]
    for i in range(n):
        num = int(input())
        while num != stack[-1]:
            if (idx == n) | (num < stack[-1]):
                return "NO"
            idx += 1
            stack.append(idx)
            ans.append("+")
        stack.pop()
        ans.append("-")
    return ans
                  
n = int(input())

answer = ss(n)
if answer == "NO":
    print(answer)
else:
    for sign in answer:
        print(sign)