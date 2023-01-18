def solution(s):
    all_chars = set(s)
    
    ans = []
    for char in all_chars:
        if list(s).count(char) == 1:
            ans.append(char)
    
    return ''.join(sorted(ans))