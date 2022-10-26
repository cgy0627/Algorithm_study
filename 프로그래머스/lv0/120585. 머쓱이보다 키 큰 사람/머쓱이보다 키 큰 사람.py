def solution(array, height):
    count = 0
    for num in array:
        if num > height:
            count += 1
    return count