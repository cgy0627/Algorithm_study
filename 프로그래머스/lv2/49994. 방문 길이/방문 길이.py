def solution(dirs):
    x,y,x1,y1 = 0,0,0,0
    paths = set()
    
    for onedir in dirs:
        if (onedir == 'U') & (y1 != 5):
            y1 += 1
        elif (onedir == 'D') & (y1 != -5):
            y1 -= 1
        elif (onedir == 'R') & (x1 != 5):
            x1 += 1
        elif (onedir == 'L') & (x1 != -5):
            x1 -= 1
        
        if (x == x1) & (y == y1):   # 안 움직임
            pass
        else:
            paths.add((x,y,x1,y1))
            paths.add((x1,y1,x,y))
        
        x, y = x1, y1
    
    return len(paths) // 2
