'''
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

'''


while True :
    num = list(map(int, input().split()))

    if all(i == 0 for i in num) :
        break
    
    else:
        a = num.pop(num.index(max(num)))
        b = num[0]
        c = num[1]
        print(num, a, b, c)

        if a**2 == b ** 2 + c ** 2:
            print('right')
        else:
            print('wrong')



