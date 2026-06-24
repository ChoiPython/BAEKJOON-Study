'''
종말의 666
'''

'''
브루트 포스 알고리즘 - 특정한 조건으로 상황을 분리하기 어렵기 때문에
하나하나 다 탐색하는 방법을 택해야함.

six(666 - 초기값)를 더하면서 n번째(= n을 더해감) 수를 찾아내야한다.
'''

n = int(input())
six = 666
cnt = 0

while True:
    # 현재 제목이 666을 포함되어있다면 cnt 카운트
    if '666' in str(six):
        cnt += 1

    # cnt가 구해야하는 n번째 영화라면 six 출력
    if cnt == n:
        print(six)
        break

    # 제목 카운트
    six += 1
                

    



