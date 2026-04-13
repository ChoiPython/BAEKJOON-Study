import sys

n = int(sys.stdin.readline())

fact = 1

for i in range(1,n+1):
    fact *= i

out = list(str(fact))

cnt = 0
for _ in range(len(out)):
    if out.pop() == '0':
       cnt += 1

    else: break 

print(cnt)