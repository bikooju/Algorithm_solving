def solution(n):
    list_x = []
    for i in range(1,n):
        if n % i == 1:
            list_x.append(i)
    return min(list_x)