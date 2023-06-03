def solution(num_list):
    prod = 1
    for num in num_list:
        prod *= num
        
    return int(prod < sum(num_list)**2)