def solution(quiz):
    answer = []
    for q in quiz:
        lst = q.split()
        ans = 0
        if lst[1] == "+":
            ans = int(lst[0]) + int(lst[2])
        else:
            ans = int(lst[0]) - int(lst[2])
        
        answer.append("O" if ans == int(lst[4]) else "X")
    
    return answer