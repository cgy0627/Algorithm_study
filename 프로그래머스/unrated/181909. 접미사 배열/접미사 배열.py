def solution(my_string):
    ans = []
    for i in range(len(my_string)):
        ans.append(my_string[i:])
    
    return sorted(ans)