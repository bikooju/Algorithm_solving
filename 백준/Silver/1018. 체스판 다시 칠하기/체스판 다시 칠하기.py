import sys
N, M = map(int,sys.stdin.readline().split())
board = [sys.stdin.readline() for _ in range(N)]


min_repaint = 64 #8x8크기 이므로 최대 64

#N : 세로
#M : 가로

for i in range(N-7):
    for j in range(M-7):
        repaint_w = 0 #맨 왼쪽 위칸이 'W'인 경우
        repaint_b = 0 #맨 왼쪽 위칸이 'B'인 경우

        for x in range(8):
            for y in range(8):
                current = board[i+x][j+y]

                expected_w = 'W' if (x+y) % 2 == 0 else 'B' #'W'로 시작
                expected_b = 'B' if (x+y) % 2 == 0 else 'W' #'B'로 시작

                if current != expected_w:
                    repaint_w += 1
                if current != expected_b:
                    repaint_b += 1

        min_repaint = min(min_repaint,repaint_w,repaint_b)
print(min_repaint)



