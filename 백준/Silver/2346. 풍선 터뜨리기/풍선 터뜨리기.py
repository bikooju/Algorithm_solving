import sys
from collections import deque

N = int(sys.stdin.readline())
moves = list(map(int, sys.stdin.readline().split()))

# 덱에 (풍선 번호, 이동값) 형태로 저장
# 풍선 번호는 1번부터 시작하므로 i+1
dq = deque((i + 1, moves[i]) for i in range(N))

result = []

while dq:  # 덱이 빌 때까지 반복
    # 맨 앞 풍선을 터뜨림
    # idx : 풍선 번호
    # k   : 그 풍선 안에 적힌 이동값
    idx, k = dq.popleft()

    # 터뜨린 풍선 번호 기록
    result.append(idx)

    # 만약 방금 터뜨린 게 마지막 풍선이면
    # 더 이상 이동할 필요가 없으므로 종료
    if not dq:
        break

    # 우리는 "이동"을 직접 하는 게 아니라
    # 다음에 터질 풍선을 덱의 맨 앞으로 가져오는 것
    # (= rotate로 회전시키는 것)

    if k > 0:
        # 오른쪽으로 k칸 이동해야 함
        # 하지만 이미 현재 풍선을 제거했기 때문에
        # 한 칸은 이미 이동한 효과가 있음
        # 따라서 k-1 만큼만 회전

        # rotate는:
        #  양수 → 오른쪽 회전
        #  음수 → 왼쪽 회전

        # 오른쪽으로 이동한 결과를 앞으로 당기려면
        # 왼쪽으로 (k-1)칸 회전해야 함
        dq.rotate(-(k - 1))

    else:
        # k가 음수라면 왼쪽으로 |k|칸 이동
        # 왼쪽 이동 결과를 앞으로 당기려면
        # 오른쪽으로 |k|칸 회전하면 됨

        # k는 음수이므로
        # -k는 양수 → 오른쪽 회전
        dq.rotate(-k)

# 결과 출력
print(*result)