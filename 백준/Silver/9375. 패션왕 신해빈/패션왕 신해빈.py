for testcase in range(int(input())):
    clothes = {}

    n = int(input())
    for i in range(n):
        clothing, clothing_type = input().split()
        if clothing_type in clothes:
            clothes[clothing_type] += 1
        else:
            clothes[clothing_type] = 2
    
    ans = 1
    for val in clothes.values():
        ans *= val
    print(ans - 1)