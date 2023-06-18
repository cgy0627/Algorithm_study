def solution(n):
    ans = []
    for i in range(n):
        new = [0] * n
        new[i] = 1
        ans.append(new)
    
    return ans