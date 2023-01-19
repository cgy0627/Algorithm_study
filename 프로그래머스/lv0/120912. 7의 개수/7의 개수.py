def solution(array):
    ans = 0
    for num in array:
        ans += list(str(num)).count('7')
    return ans