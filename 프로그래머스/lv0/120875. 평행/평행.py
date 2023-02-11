def solution(dots):
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            a,b = {0,1,2,3} - {i,j}
            
            if (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0]) == (dots[a][1] - dots[b][1]) / (dots[a][0] - dots[b][0]):
                return 1
    
    return 0