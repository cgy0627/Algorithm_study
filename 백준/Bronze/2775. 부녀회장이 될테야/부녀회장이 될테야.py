for i in range(int(input())):
    k, n = int(input()), int(input())
    apt = [[0 for i in range(n)] for i in range(k+1)]
    apt[0] = [i for i in range(1, n+1)]

    for floor in range(1, k+1):
        for ho in range(0, n):
            apt[floor][ho] = sum(apt[floor-1][:ho+1])
    
    print(apt[k][n-1])