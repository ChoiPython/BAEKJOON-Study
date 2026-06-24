'''

“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 

주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.


'''
import sys
t = int(sys.stdin.readline())

def floor(k, n, before, next) :
    next.clear()

    for i in range(1, k + 1) :
        for j in range(1, n + 1):
            next.append(sum(before[:j]))
        
        before = next.copy()
        if i != k:
            del(next[:n])
        
    return next, before


out = []
for i in range(t) :
    k = int(input())
    n = int(input())
        
    before = [a for a in range(1, 15)]  # 1 ~ 14
    next = []


    next, before = floor(k, n, before, next)
    out.append(next[-1])

for j in out :
    print(j)






