def solution(A, B):
    rounds = 0
    for i in range(len(A)):
        print(A)
        if A == B:
            return rounds
        else:
            A = A[-1] + A[:-1]
            rounds += 1
            
    return -1