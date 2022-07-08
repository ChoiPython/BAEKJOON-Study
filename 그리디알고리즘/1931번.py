'''한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
 
 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
 
 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.'''

''' 힌트 - (1,4), (5,7), (8,11), (12,14) 를 이용할 수 있다. '''

# def start_meet(start, m):      # 제일 처음 회의 시간
#     for j in range(len(m)):
#         if start[2] > m[j][2] :
#             start = m[j]
#     return start

n = int(input())    # 회의 개수

m = list()          # 1 4 / 3 5 / 0 6 / 5 7 / 3 8 / 5 9 / 6 10 / 8 11 / 8 12 / 2 13 / 12 14

for i in range(n) :
    x, y = map(int, input().split())

    m.append([x, y, y-x])   # 시작, 끝, 회의 시간
    m.sort()                # 시작 시간 기준 정렬
# print(m)
# start = m[0]                # 첫 회의 테스트
count = 1                   # 시작 회의 -> 카운트 0
max_count = -1

for i in range(len(m)) :
    start = m[i]
    print(start, 'start_val')
    for j in range(len(m)):

        if start[1] <= m[j][0] :            # 시작시간 작은 수가 시작할 때 : 순차적으로 회의 배정
            start = m[j]
            count += 1
            print('count += 1')

        # elif start[0] >= m[j][1]  :            # 시작시간 큰 수가 시작할 때 : 뒷 시간 가능한 시간 넣기
        #     count += 1
        #     print(count, end = 'ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡelif\n')
        #     continue

        else:
            print('???')
        print(count, end = 'ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n')

    if max_count < count :
        max_count = count
        print(max_count, ': max_count')

    count = 1
    


print(max_count)









        # print(start)       
        
        # if m[j][0] >= start[1] :
        #     start = m[j]
        #     count += 1







