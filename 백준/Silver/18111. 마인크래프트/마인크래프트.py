import sys

# 입력 받기
N, M, B = map(int, sys.stdin.readline().split())
land = []
for _ in range(N):
    land.extend(map(int, sys.stdin.readline().split()))

height_count = [0] * 257  # 높이별 블록 개수 카운트
for h in land:
    height_count[h] += 1

min_time = float('inf')
best_height = 0

# 가능한 모든 높이 시도 (0~256)
for target in range(257):
    remove_blocks = 0  # 제거해야 하는 블록 개수
    add_blocks = 0  # 추가해야 하는 블록 개수

    for height in range(257):
        if height > target:
            remove_blocks += (height - target) * height_count[height]
        elif height < target:
            add_blocks += (target - height) * height_count[height]

    # 인벤토리에 충분한 블록이 있는 경우만 수행 가능
    if remove_blocks + B >= add_blocks:
        time = remove_blocks * 2 + add_blocks
        if time < min_time or (time == min_time and target > best_height):
            min_time = time
            best_height = target

print(min_time, best_height)
