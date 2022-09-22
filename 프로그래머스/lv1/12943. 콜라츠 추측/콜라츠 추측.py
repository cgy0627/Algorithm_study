def solution(num):
    rounds = 0
    while rounds < 500:
        if num == 1:
            return rounds
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1
        
        rounds += 1
    
    return -1
        
#     def rounds(n):
#         if n == 1:
#             return 1
#         if n % 2 == 0:      # even number
#             return 1 + rounds(n//2)
#         if n % 2 == 1:      # odd number
#             return 1 + rounds((n*3)+1)
    
#     return rounds(num)