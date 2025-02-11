def solution(nums):
    answer = 0
    pick = int(len(nums)/2)
    count = len(set(nums))
    
    if pick < count:
        return pick
    else:
        return count