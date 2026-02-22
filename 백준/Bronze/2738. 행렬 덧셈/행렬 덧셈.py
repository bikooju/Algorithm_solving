import sys
N, M = map(int, sys.stdin.readline().split())
A_matrix = []
B_matrix = []

for i in range(N):
    A_matrix.append(list(map(int, sys.stdin.readline().split()))) # A[0]에 리스트가 들어감

for i in range(N):
    B_matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        print(A_matrix[i][j] + B_matrix[i][j], end=" ")
    print()