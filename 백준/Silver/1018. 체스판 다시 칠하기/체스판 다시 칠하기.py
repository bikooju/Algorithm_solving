import sys

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]  # 입력값 개행 문자 제거

min_repaint = 64  # 8x8에서 최대 64칸 다시 칠할 수 있음

for i in range(N - 7):  # 세로 방향 이동
    for j in range(M - 7):  # 가로 방향 이동
        repaint_w = 0  # 왼쪽 위가 'W'인 경우 다시 칠해야 하는 개수
        repaint_b = 0  # 왼쪽 위가 'B'인 경우 다시 칠해야 하는 개수

        for x in range(8):  # 8x8 크기만큼 탐색
            for y in range(8):  # 8x8 크기만큼 탐색
                # 현재 위치의 원래 색
                current = board[i + x][j + y]
                # 올바른 체스판 패턴에서 예상되는 색
                expected_w = 'W' if (x + y) % 2 == 0 else 'B'
                expected_b = 'B' if (x + y) % 2 == 0 else 'W'

                # 예상 색과 다르면 다시 칠하기
                if current != expected_w:
                    repaint_w += 1
                if current != expected_b:
                    repaint_b += 1

        # 최소값 갱신
        min_repaint = min(min_repaint, repaint_w, repaint_b)

print(min_repaint)
