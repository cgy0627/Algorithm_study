def solution(number):
    ans = 0
    for i in range(len(number)-1):
        for k in range(i+1, len(number)):
            ans += number[k+1:].count(0 - number[i] - number[k])
    
    return ans