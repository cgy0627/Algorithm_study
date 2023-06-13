def solution(num_list):
    y, z = num_list[-2], num_list[-1]
    
    return num_list + [z - y] if z > y else num_list + [z * 2]