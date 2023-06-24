def solution(date1, date2):
    return int(int(''.join(map(str, date1))) < int(''.join(map(str, date2))))