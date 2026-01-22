import sys

N = int(sys.stdin.readline())
d = len(str(N))
start = max(1, N - 9 * d)

answer = 0
for M in range(start, N):
    digit_sum = sum(map(int, str(M)))
    if M + digit_sum == N:
        answer = M
        break

print(answer)
