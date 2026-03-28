import sys
N = int(sys.stdin.readline().rstrip())
N_list = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
M_list = list(map(int, sys.stdin.readline().split()))

# M_list 수들(m)이 N_list에 존재하는지 보기
for m in M_list:
    if m in N_list:
        print("1")
    else:
        print("0")