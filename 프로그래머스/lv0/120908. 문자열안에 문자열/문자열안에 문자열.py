def solution(str1, str2):
    try:
        str1.index(str2)
    except:
        return 2
    else:
        return 1