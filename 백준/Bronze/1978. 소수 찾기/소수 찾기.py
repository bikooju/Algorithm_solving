import sys
N = sys.stdin.readline()
num_list = list(map(int, sys.stdin.readline().split()))
count = 0 # 소수 세기
for num in num_list:
    if num == 1:
        continue

    is_prime = True
    for j in range(2, num):
        if num % j == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

print(count)