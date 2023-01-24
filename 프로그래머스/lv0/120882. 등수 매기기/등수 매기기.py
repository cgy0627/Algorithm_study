def solution(score):
    score_sort = sorted(list(map(lambda x: sum(x)/len(x), score)), reverse=True)
    return [score_sort.index(sum(s)/len(s))+1 for s in score]