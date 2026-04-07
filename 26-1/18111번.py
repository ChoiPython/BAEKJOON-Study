'''
첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)
둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. 
(i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 
땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.
'''

import sys

n, m, b = map(int, sys.stdin.readline().split())

heights = []
for _ in range(n):
    heights.extend(map(int, sys.stdin.readline().split()))

# 높이별 빈도수 계산 
count = [0] * 257
for h in heights:
    count[h] += 1

min_time = float('inf')
best_height = 0

for target in range(257):
    removed = 0 # 블럭 제거
    added = 0   # 쌓을 블럭

    # 전체 칸을 도는 게 아니라, 0~256층 종류만 확인한다?
    for h in range(257):
        if count[h] == 0: continue

        if h > target:
            removed += (h-target) * count[h]

        else:
            added += (target - h) * count[h]

    # 인벤토리 체크 및 최솟값 갱신
    if removed + b >= added:
        time = removed * 2 + added

        if time <= min_time:
            min_time = time
            best_height = target

print(min_time, best_height)
