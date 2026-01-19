import sys
while True:
    N_list = list(map(int, sys.stdin.readline().split()))
    c = max(N_list)
    sum = 0
    for n in N_list:
        if n != c:
            sum += n**2

    if sum == 0:
        break
    elif sum == c**2:
        print("right")
    else:
        print("wrong")