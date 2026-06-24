'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 

상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

'''




n = int(input())
my = list(map(int, input().split()))


m = int(input())
your = list(map(int, input().split()))

count = {}

# 딕셔너리에 저장
for i in my :
    if i in count :
        count[i] += 1

    else:
        count[i] = 1


for i in your :
    if i in count :
        print(count[i], end = ' ')

    else:
        print(0, end = ' ')




