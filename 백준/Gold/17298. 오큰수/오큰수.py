import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
stack = [] #오큰수를 찾기 위해 인덱스를 담을 스택
answer = [-1] * N #기본이 -1
#오큰수 : A의 오큰수는 오른쪽에 있고 A보다 큰 수중에서 가장 왼쪽에 있는 수
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer) #결과 리스트를 공백으로 구분하여 출력
