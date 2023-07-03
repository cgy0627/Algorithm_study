def solution(my_string, m, c):
    ans = ''
    count = 0
    for char in my_string:
        count += 1
        if count == c:
            ans += char
        if count == m:
            count = 0
    
    return ans