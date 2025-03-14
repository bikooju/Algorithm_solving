import sys

# 입력값을 빠르게 받기 위한 설정
input = sys.stdin.read
data = input().split("\n")

# 1. 입력 처리
n, m = map(int, data[0].split())  # 종이 크기 (N x M)
graph = [list(map(int, data[i + 1].split())) for i in range(n)]  # 종이에 적힌 숫자 저장
visited = [[False] * m for _ in range(n)]  # 방문 여부를 체크하는 배열

# 2. 방향 벡터 설정 (상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 최댓값 저장 변수
maximum = 0

# 3. DFS 탐색 함수 (ㅗ 모양 제외)
def dfs(x, y, tmp, cnt):
    """
    깊이 우선 탐색(DFS)을 통해 ㅗ 모양을 제외한 테트로미노 모양을 탐색하는 함수
    x, y: 현재 위치
    tmp: 현재까지 더한 값
    cnt: 현재까지 선택한 칸 개수 (4개가 되면 종료)
    """
    global maximum
    if cnt == 4:  # 정사각형 4개를 선택한 경우
        maximum = max(maximum, tmp)  # 최댓값 갱신
        return

    for i in range(4):  # 네 방향으로 이동
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나거나 이미 방문한 경우 스킵
        if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
            continue

        # 방문 처리 후 DFS 탐색
        visited[ny][nx] = True
        dfs(nx, ny, tmp + graph[ny][nx], cnt + 1)
        visited[ny][nx] = False  # 백트래킹 (원래 상태로 되돌리기)

# 4. ㅗ 모양 탐색 함수 (DFS로는 찾을 수 없는 경우)
def fy(x, y):
    """
    ㅗ, ㅜ, ㅓ, ㅏ 모양을 탐색하는 함수
    x, y: 현재 위치 (중심점)
    """
    global maximum
    tmp = graph[y][x]  # 현재 위치 값
    arr = []

    for i in range(4):  # 4방향을 확인
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나면 스킵
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        arr.append(graph[ny][nx])

    length = len(arr)  # 가능한 방향 개수

    if length == 4:  # 4방향 모두 존재하는 경우
        arr.sort(reverse=True)  # 가장 작은 값을 제거하여 ㅗ 모양을 만든다.
        arr.pop()
        maximum = max(maximum, sum(arr) + graph[y][x])

    elif length == 3:  # 3방향만 존재하는 경우
        maximum = max(maximum, sum(arr) + graph[y][x])

# 5. 모든 위치에서 테트로미노 배치 시도
for i in range(n):
    for j in range(m):
        visited[i][j] = True  # 현재 위치 방문 표시
        dfs(j, i, graph[i][j], 1)  # DFS 실행 (ㅗ 모양 제외)
        fy(j, i)  # ㅗ 모양 탐색
        visited[i][j] = False  # 방문 해제 (백트래킹)

# 6. 최댓값 출력
print(maximum)
