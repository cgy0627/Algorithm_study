def solution(arr1, arr2):
    ans = [[0 for i in range(len(arr1[0]))] for j in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            ans[i][j] = arr1[i][j] + arr2[i][j]
            
    return ans