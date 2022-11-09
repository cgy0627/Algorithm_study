def solution(numbers):
    numbers = sorted(numbers)
    return numbers[-1] * numbers[-2]