import sys
N = int(sys.stdin.readline().rstrip())
count = 0

for i in range(1,N+1):
    num_list = list(map(int,str(i)))
    if i < 100:
        count += 1 #100보다 작으면 모두 한수
    else:
        if (num_list[0] - num_list[1]) == (num_list[1] - num_list[2]):
            count += 1 #x의 각 자리가 등차수열이면 한수

print(count)
