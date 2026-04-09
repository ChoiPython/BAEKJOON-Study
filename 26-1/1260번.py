import sys
from collections import deque

# 1. 입력 받기 및 그래프 초기화
input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 작은 번호부터 방문하기 위해 정렬
for i in range(1, n + 1):
    graph[i].sort()

# 2. DFS 구현 (재귀)
def dfs(now):
    visited_dfs[now] = True
    print(now, end=' ')
    for next_node in graph[now]:
        if not visited_dfs[next_node]:
            dfs(next_node)

# 3. BFS 구현 (큐)
def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for next_node in graph[now]:
            if not visited_bfs[next_node]:
                visited_bfs[next_node] = True
                queue.append(next_node)

# 탐색 전 방문 배열 초기화
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# 결과 출력
dfs(v)
print() # 줄바꿈
bfs(v)