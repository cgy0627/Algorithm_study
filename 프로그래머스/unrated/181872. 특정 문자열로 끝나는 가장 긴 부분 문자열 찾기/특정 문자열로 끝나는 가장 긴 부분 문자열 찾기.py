def solution(myString, pat):
    k = len(pat)
    match = 0
    for i in range(len(myString)-k+1):
        if myString[i:i+k] == pat:
            match = i

    return myString[:match+k]