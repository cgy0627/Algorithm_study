def solution(dot):
    if (dot[0] > 0) & (dot[1] > 0):
        return 1
    elif (dot[0] > 0) & (dot[1] < 0):
        return 4
    elif (dot[0] < 0) & (dot[1] < 0):
        return 3
    elif (dot[0] < 0) & (dot[1] > 0):
        return 2