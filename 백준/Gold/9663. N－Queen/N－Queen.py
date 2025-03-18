import sys

def backtrack(row):
    global count
    if row == N:  # 모든 퀸을 배치한 경우
        count += 1
        return

    for col in range(N):
        if columns[col] or diagonal1[row - col + N - 1] or diagonal2[row + col]:
            continue  # 유효하지 않으면 건너뛰기

        # 현재 위치에 퀸 배치
        columns[col] = True
        diagonal1[row - col + N - 1] = True
        diagonal2[row + col] = True

        # 다음 행 탐색
        backtrack(row + 1)

        # 백트래킹 (되돌아가기)
        columns[col] = False
        diagonal1[row - col + N - 1] = False
        diagonal2[row + col] = False

# 입력 받기
N = int(sys.stdin.readline().strip())

# 전역 변수 초기화
count = 0
columns = [False] * N  # 같은 열 차지하는지 여부
diagonal1 = [False] * (2 * N - 1)  # ↘↖ 대각선 체크 (row - col)
diagonal2 = [False] * (2 * N - 1)  # ↙↗ 대각선 체크 (row + col)

# 백트래킹 시작
backtrack(0)

# 결과 출력
print(count)
