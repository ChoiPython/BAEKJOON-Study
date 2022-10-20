'''

제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

'''
#
'''
https://pacific-ocean.tistory.com/61 - 규칙성을 발견하고 n에 대하여 그냥 바로 출력
a = int(input())
b = 2
while True:
    if a == 1 or a == 2:
        print(a)
        break
    b *= 2
    if b >= a:
        print((a - (b // 2)) * 2)
        break
'''

''' 내가 만든 덱
def deque(num, stop) :
    if stop:
        num.pop(0)
        return num

    else:
        num.pop(0)
        push = num.pop(0)
        num.append(push)
        return num

n = int(input())

num = [a for a in range(1, n + 1)]
stop = False
count = 1 # n // 2 + 1

while True:
    if n < 3:
        print(n)
        exit()

    if stop == True:
        break

    else:
        if count == n - 1:
            stop = True
            deque(num, stop)

        else:   
            num = deque(num, stop)

        count += 1

print(num[0])

'''


''' 덱 라이브러리 불러옴
from collections import deque

d = deque()
n = int(input())

# 덱에 추가
for i in range(1, n + 1) :
    d.append(i)     # appnedleft - 왼쪽 부터 삽입
                    # extend(left)[1, 2, 3] - 한번에 추가

while len(d) != 1 :
    d.popleft()
    d.append(d.popleft())

print(d[0])
'''

'''?? 리스트랑 뭐가 다르지

n= int(input())
num = []

for i in range(1, n + 1):
    num.append(i)

while len(num) != 1:
    num.pop(0)
    num.append(num.pop(0))

print(num[0])
'''