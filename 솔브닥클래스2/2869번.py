'''
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

'''

a, b, v = map(int, input().split())

val = (v - a) // (a - b)

if a - b == 1 :
    print(v - b)

elif a * val - b * val >= v - a :
    print(val + 1)
    pass

else :
    print(val + 2)
    pass


'''
---실패---
def test(val, v) :
    result = v / val
    if result > v // val :
        result += 1 - (result - v // val) # 소수점 존재 시 무조건 반올림

    return int(result)

a, b, v = map(int, input().split())

am = test(a, v)

if a - b == 1 :
    print(v - b)

else:

    if a * am - b * (am - 1) > v :
        result = am
        pass

    else :
        result = am + 1

    print(result)
'''