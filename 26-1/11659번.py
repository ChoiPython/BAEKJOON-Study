import sys

n, m = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

# 누적 합 배열 만들기
prefix = [0]
temp = 0
for i in num:
    temp += i
    prefix.append(temp)

for _ in range(m):
    out = 0
    i, j = map(int, sys.stdin.readline().split())

    print(prefix[j]-prefix[i-1])   
