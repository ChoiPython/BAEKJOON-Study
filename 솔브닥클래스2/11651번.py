'''
2차원 평면 위의 점 N개가 주어진다. 
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

'''
import sys

n =  int(sys.stdin.readline())

point = [list(map(int, input().split())) for i in range(n)]

point.sort(key = lambda x : (x[1], x[0]))

for i in range(len(point)) :
    print(point[i][0], point[i][1])



