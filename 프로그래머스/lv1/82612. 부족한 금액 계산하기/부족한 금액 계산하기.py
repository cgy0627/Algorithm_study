def solution(price, money, count):
    required = sum([price * i for i in range(1, count+1)])
    if required > money:
        return required - money
    else:
        return 0