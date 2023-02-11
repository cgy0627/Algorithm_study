def solution(lines):
    total_line = [0] * 201
    for s,e in lines:
        for i in range(s+100, e+100):
            total_line[i] += 1
    
    return 201 - total_line.count(0) - total_line.count(1)