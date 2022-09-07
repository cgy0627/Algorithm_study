def solution(seoul):
    for i, n in enumerate(seoul):
        if n == "Kim":
            return f'김서방은 {i}에 있다'