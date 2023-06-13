def solution(num_list):
    def prod(num_list):
        ans = 1
        for num in num_list:
            ans *= num
        return ans
    
    return sum(num_list) if len(num_list) > 10 else prod(num_list)