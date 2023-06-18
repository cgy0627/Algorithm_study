def solution(strArr):
    ans = []
    for word in strArr:
        if 'ad' not in word:
            ans.append(word)
    
    return ans