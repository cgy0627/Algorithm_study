def solution(numbers):
    num_dict = dict(zip(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], range(0,10)))
    
    for k,v in num_dict.items():
        numbers = numbers.replace(k, str(v))
        
    return int(numbers)