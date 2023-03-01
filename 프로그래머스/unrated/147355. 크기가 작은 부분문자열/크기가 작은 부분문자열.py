def solution(t, p):
    count = 0
    for i in range(0, len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            print(t[i:i+len(p)])
            count += 1
    
    return count