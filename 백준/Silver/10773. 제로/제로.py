import sys
K = int(sys.stdin.readline().rstrip())
num_list = []
sum = 0

for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)

for i in num_list:
    sum += i

print(sum)

