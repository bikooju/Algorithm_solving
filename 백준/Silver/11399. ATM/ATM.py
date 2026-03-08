import sys
N = int(sys.stdin.readline())
sum = 0
result = 0
pi_list = list(map(int, sys.stdin.readline().split())) # [3,1,4,3,2]
pi_list.sort() # [1,2,3,3,4]
sum_list = []
for i in pi_list:
    sum += i
    sum_list.append(sum) # 0+1, 1+2,  1+2+3, 1+2+3+3, 1+2+3+3+4

for i in sum_list: #[1, 3, 6, 9, 13]
    result += i

print(result)