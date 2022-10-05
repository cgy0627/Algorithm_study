def recursion(s, l, r, rounds):
    if l >= r: 
        return 1, rounds
    elif s[l] != s[r]: 
        return 0, rounds
    else: 
        return recursion(s, l+1, r-1, rounds+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

n = int(input())

for i in range(n):
    s = input()
    res, rounds = isPalindrome(s)
    print(res, rounds)