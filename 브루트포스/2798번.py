'''
1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)x1,000원의 상금을 받게 된다.
2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)x100원의 상금을 받게 된다.
3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)x100원의 상금을 받게 된다.

'''

dice = list(map(int, input().split()))

if dice[0] == dice[1] == dice[2] :     # 3개가 동일 할 경우
    print(10000 + dice[0] * 1000)

    pass

# 둘중 하나만 같을 경우
elif dice[0] == dice[1] :     
    print(1000 + dice[0] * 100)
    pass

elif dice[0] == dice[2]:
    print(1000 + dice[0] * 100)
    pass

elif dice[1] == dice[2]:
    print(1000 + dice[1] * 100)
    pass

else:
    print(max(dice) * 100)  # 다 다를 경우
