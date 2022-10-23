def solution(numbers):
    return sorted(list(set(numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers)))))
    