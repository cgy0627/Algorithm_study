def solution(n, words):
    turns = [0] * n
    
    prev = words[0]
    turns[0] += 1
    for i in range(1, len(words)):
        print(words[i])
        if (words[i] in words[:i]) | (words[i][0] != prev[-1]):
            return [i % n + 1, turns[i%n]+1]
        else:
            prev = words[i]
            turns[i%n] += 1
    
    return [0,0]