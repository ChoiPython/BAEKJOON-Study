
'''
     1   2   3
1|   0   1   0       => 1이랑 2랑 연결 -> 1이랑 연결된 개수만 세면 끝
2|   1   0   1       => 2랑 3이랑 연결
3|   0   1   0       => 2랑 3이랑 연결

'''

'''
인접 리스트 방식
1번 노드에 연결되 노드를 같은 리스트에 저장
즉, 1번이랑 연결된 노드: 2, 3, 4
matrix[0] = [2, 3, 4]           # index는 0임을 주의
maxtrix = [[2, 3, 4], ....]
'''

computers = int(input())
pair = int(input())
visited = [False] * computers
matrix = [[0]*computers for _ in range(computers)]   # 인접 리스트 생성 

for _ in range(pair):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

# DFS
cnt = 0
def dfs(now):
    global cnt
    visited[now] = True
    for next_node in range(computers):
        if matrix[now][next_node] == 1 and not visited[next_node]:
            cnt += 1
            dfs(next_node)

dfs(0)
print(cnt)
    





