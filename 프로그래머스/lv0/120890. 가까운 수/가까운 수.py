def solution(array, n):
    array.sort()
    for i in range(len(array)):
        if array[i] > n:
            if (array[i] - n) < (n - array[i-1]):
                return array[i]
            else:
                return array[i-1]
    
    return array[-1]