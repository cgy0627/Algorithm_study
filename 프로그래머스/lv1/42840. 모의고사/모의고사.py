def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    first = first * (len(answers) // len(first)) + first[:len(answers)%len(first)]
    second = second * (len(answers) // len(second)) + second[:len(answers)%len(second)]
    third = third * (len(answers) // len(third)) + third[:len(answers)%len(third)]
    
    first_ans = sum([first[i] == answers[i] for i in range(len(answers))])
    second_ans = sum([second[i] == answers[i] for i in range(len(answers))])
    third_ans = sum([third[i] == answers[i] for i in range(len(answers))])
    
    res = []
    for i, ans in enumerate([first_ans, second_ans, third_ans]):
        if ans == max(first_ans, second_ans, third_ans):
            res.append(i+1)
    
    return res