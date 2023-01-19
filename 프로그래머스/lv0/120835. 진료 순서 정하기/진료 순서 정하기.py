def solution(emergency):
    emergency_sort = sorted(emergency, reverse=True)
    return [emergency_sort.index(num) + 1 for num in emergency]
    