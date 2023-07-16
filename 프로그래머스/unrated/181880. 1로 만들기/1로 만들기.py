def solution(num_list):
    history = [0 for i in range(max(num_list) + 1)]
    history[2], history[3] = 1, 1
    for i in range(4, len(history)):
        if i % 2 == 0:
            history[i] = history[i // 2] + 1
        else:
            history[i] = history[(i - 1) // 2] + 1
    
    return sum([history[n] for n in num_list])