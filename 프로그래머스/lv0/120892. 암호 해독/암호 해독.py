def solution(cipher, code):
    ans = ''
    for i in range(code, len(cipher)+1, code):
        ans += cipher[i-1]
    return ans