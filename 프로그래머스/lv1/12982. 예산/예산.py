import heapq
def solution(d, budget):
    count = 0
    heapq.heapify(d)
    for i in range(len(d)):
        budget -= heapq.heappop(d)
        if budget < 0:
            break
        print(budget)
        count += 1
    
    return count