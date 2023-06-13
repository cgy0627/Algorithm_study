def solution(myString, pat):
    return int(pat in myString.replace('A', 'b').replace('B', 'a').upper())