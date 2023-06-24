def solution(my_string, indices):
    ans = list(my_string)
    for i in indices:
        ans[i] = ''
    
    return ''.join(ans)