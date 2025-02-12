def solution(participant, completion):
    dt = {}
    sum_hash = 0
    
    for i in participant:
        dt[hash(i)] = i
        sum_hash += hash(i)
    
    for j in completion:
        sum_hash -= hash(j)
    
    return dt[sum_hash]