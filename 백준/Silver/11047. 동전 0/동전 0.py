import sys
N, K = map(int, sys.stdin.readline().split())
N_list = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
count = 0 # 동전 개수
max_n_count = 0
lower_K = []



#max_n 구하기
for n in N_list:
    if n > K:
        break
    lower_K.append(n) # [1,5,10,50,100]


while K > 0:
    # K : 200, max(lower_K): 100
    if K >= max(lower_K):
        # max_n을 몇개 곱할 수 있을지 (4200 / 1000 > 1)
        max_n_count = K // max(lower_K)  # 200 // 100 => 2
        K = K - (max(lower_K) * max_n_count)  # 200 - 100 * 2 = 0
        count = count + max_n_count # count = 4 + 2 = 6

    lower_K.pop() # 현재 최댓값 제거

    if K == 0:
        break

print(count)
