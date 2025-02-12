def solution(participant, completion):
    dt = {}
    sum_hash = 0
    
    for i in participant:
        dt[hash(i)] = i
        sum_hash += hash(i)
    
    for j in completion:
        sum_hash -= hash(j)
    
    return dt[sum_hash]

from collections import Counter

def solution(participant, completion):
    answer=''
    dict_result = Counter(participant) - Counter(completion)
    return list(dict_result.keys())[0]
    
