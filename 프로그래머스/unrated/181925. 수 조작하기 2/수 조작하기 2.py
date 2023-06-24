def solution(numLog):
    control = {1:'w', -1:'s', 10:'d', -10:'a'}
    return ''.join(map(lambda i: control[numLog[i] - numLog[i-1]], range(1, len(numLog))))