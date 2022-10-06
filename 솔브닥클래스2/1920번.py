'''
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 

이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
'''
import time
# 존재하면 1 else - 0
n = int(input())

A = set(map(int, input().split()))
A = list(A)

m = int(input())
data = list(map(int, input().split()))

# 정렬
A.sort()

for i in data:
    Check = False    # True = 1 / False = 0

    last = len(A) - 1
    start = 0

    while start <= last:
        # 중간값
        mid_index = (last + start) // 2
        
        # 중간값 = 비교 데이터
        if A[mid_index] == i :
            print(1)
            Check = True
            break

        # 중간값 수정 - 반씩 쪼개가면서 비교 데이터 찾기
        elif A[mid_index] > i :     # 중간값이 비교 데이터보다 클 경우
            last = mid_index - 1

        else:     # 중간값이 비교 데이터보다 작을 경우
            start = mid_index + 1

    if Check == False:
        print(0)
        
        
