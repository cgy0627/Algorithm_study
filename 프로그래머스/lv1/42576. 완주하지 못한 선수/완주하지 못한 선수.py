def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        last_part = participant.pop()
        last_comp = completion.pop()
        
        if last_part != last_comp:
            return last_part
    
    return participant[0]
        