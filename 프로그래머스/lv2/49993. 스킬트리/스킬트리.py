def solution(skill, skill_trees):
    from collections import deque
    
    ans = 0
    for st in skill_trees:
        ans += 1
        check = deque(skill)
        for char in st:
            if char in check:
                if char == check[0]:
                    check.popleft()
                else:
                    ans -= 1
                    break
                
    return ans