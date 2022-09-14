'''

한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 

왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 

직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

'''

from math import sqrt

x, y, w, h = map(int, input().split())

row1 = abs(w - x)       # 오른쪽 벽
row2 = abs(0 - x)       # 왼쪽 벽
col1 = abs(h - y)        # 아래 벽
col2 = abs(0 - y)        # 윗 벽

minx = row1             # x, y 최소 거리
if minx > row2 :
    minx = row2

miny = col1
if miny > col2 :
    miny = col2

# 출력 최소거리

out = minx
if out > miny :
    out = miny

print(out)






