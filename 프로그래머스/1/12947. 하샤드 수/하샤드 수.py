def solution(x):
    lst = list(str(x))
    total = sum(int(num) for num in lst)
    if x % total == 0:
        return True
    return False