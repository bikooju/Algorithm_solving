import sys
from collections import deque
matrix = []
max_num = 0
i_location = 0
j_location = 0
result = deque()

for _ in range(9):
        matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if max_num <= matrix[i][j]:
            max_num = matrix[i][j]
            i_location = i + 1
            j_location = j + 1

print(max_num)
print(i_location, j_location)