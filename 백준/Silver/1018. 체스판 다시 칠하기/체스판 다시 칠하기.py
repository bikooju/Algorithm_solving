N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 정답 초기값을 매우 큰 숫자로 설정
min_repaint = 64  # 8x8에서 최대 64칸을 다시 칠할 수 있음

# 8x8 체스판을 만들 수 있는 모든 시작 위치 탐색
for i in range(N - 7):
    for j in range(M - 7):
        repaint_w = 0  # 왼쪽 위가 'W'인 경우 다시 칠해야 하는 개수
        repaint_b = 0  # 왼쪽 위가 'B'인 경우 다시 칠해야 하는 개수
        
        for x in range(8):
            for y in range(8):
                # 현재 위치의 원래 색
                current = board[i + x][j + y]
                # 올바른 체스판 패턴에서 예상되는 색
                expected_w = 'W' if (x + y) % 2 == 0 else 'B'
                expected_b = 'B' if (x + y) % 2 == 0 else 'W'
                
                # 만약 예상되는 색과 다르면 다시 칠해야 함
                if current != expected_w:
                    repaint_w += 1
                if current != expected_b:
                    repaint_b += 1
        
        # 최소값 갱신
        min_repaint = min(min_repaint, repaint_w, repaint_b)

print(min_repaint)