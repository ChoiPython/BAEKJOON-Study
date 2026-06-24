import sys

n, m = map(int, sys.stdin.readline().split())

cnt = 0
out = []

def dfs(start):

    if len(out) == m:
        print(*out)
        return
    
    for i in range(start, n+1):
        out.append(i)
        dfs(i)
        out.pop()

dfs(1)
        


    


            














