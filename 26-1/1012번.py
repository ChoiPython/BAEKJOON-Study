'''

'''

import sys
sys.setrecursionlimit(10**6)
    
def dfs(x, y):
    # 상, 하, 좌, 우 방향 벡터
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 현재 배추 위치를 방문 처리
    farmland[y][x] = 0

    # 네 방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 지도 범위 안에 있고, 그 위치에 배추(1)가 있다면 탐색 진행
        if (0 <= nx < m) and (0 <= ny <n) :
            if farmland[ny][nx] == 1:
                dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())        # m: 가로, n: 세로 k: 배추 개수
    farmland = [[0]*m for _ in range(n)]
    worm = 0

    for _ in range(k):
        x, y = map(int, input().split())
        farmland[y][x] = 1 

    for i in range(m):
        for j in range(n):
            if farmland[j][i] == 1:
                dfs(i, j)
                worm += 1

    print(worm)








            



    
    
    