def solution(a, b):
    days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    week = {1: 'SUN', 2: 'MON', 3: 'TUE', 4: 'WED', 5: 'THU', 6: 'FRI', 0: 'SAT'}
    
    new_year = 6
    
    total = 0
    for i in range(1, a):
        total += days[i]
    
    total += b
    
    day = int((total - 1 + new_year) % 7)
    print(total, day, week[day])
    
    return week[day]
    