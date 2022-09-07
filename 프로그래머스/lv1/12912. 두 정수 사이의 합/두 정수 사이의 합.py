def solution(a, b):
    answer = 0
    
    if a > b:
        answer = sum(range(b, a + 1))
    elif b > a:
        answer = sum(range(a, b + 1))
    elif a == b:
        return a
    
    return answer