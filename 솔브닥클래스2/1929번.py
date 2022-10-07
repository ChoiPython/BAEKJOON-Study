'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
        에라토스테네스의 체
'''
import sys

M, N = map(int, sys.stdin.readline().split())

# 어떤 수의 제곱근
for i in range(M, N + 1) :  # 2 ~ N+1
    if i == 1 :
        continue

    for j in range(2, int(i**0.5) + 1) :
        if i % j == 0:
            break

    else:
        print(i)


    
# 에라토스테네스의 체 단순 반복 - 전체 탐색
# data = [data for data in range(2, N + 1)]
# for i in range(2, N + 1) :  # 2 ~ N+1
#     mul = 1

#     if i < M :
#         while i * mul in data:
#             data.remove(i * mul)
#             mul += 1
        
#     else:
#         while i * mul <= N:
#             if mul == 1 and i in data:
#                 mul += 1
#                 print(i)
#                 data.remove(i)

#             else: 
#                 try:
#                     data.remove(i * mul)
#                     mul += 1
                    
#                 except:
#                     mul += 1
