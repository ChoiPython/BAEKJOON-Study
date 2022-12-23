'''
플레이어가 5, 6번 승리시 그룹1
플레이어가 3, 4번 승리시 그룹2
플레이어가 1, 2번 승리시 그룹3

'''
result = [input() for i in range(6)]

if result.count("W") > 4 :
    print(1)

elif result.count("W") > 2 :
    print(2)

elif result.count("W") > 0 :
    print(3)

else:
    print(-1)



