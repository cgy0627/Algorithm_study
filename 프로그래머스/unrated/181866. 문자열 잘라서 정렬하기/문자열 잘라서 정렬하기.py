def solution(myString):
    ans = sorted(myString.strip('x').split('x'))
    
    return [x for x in ans if x]