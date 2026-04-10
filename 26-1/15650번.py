import sys

n, m = map(int, sys.stdin.readline().split())

out = []
def dfs(start, count):
    if count == m:
        for j in range(len(out)):
            print(out[j]+1, end=" ")
        print()

    for i in range(start, n):
        out.append(i)
        dfs(i+1, count+1)
        out.pop()
dfs(0,0)
