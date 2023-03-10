'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
# import sys 

# n = int(sys.stdin.readline())
# num = [int(sys.stdin.readline()) for i in range(n)]

# count = [0] * (max(num) + 1)


# # 개수 세기
# for i in num :
#     count[i] += 1

# for i in range(len(count)) :
#     if count[i] != 0 :
#         for j in range(count[i]) :
#             print(i)

# num에 입력받는 즉시 count에 추가할 수 있다!! .. 대박!


import sys 

n = int(sys.stdin.readline())

count = [0] * 10001

# 개수 세기
for i in range(n) :
    count[int(sys.stdin.readline())] += 1

for i in range(len(count)) :
    if count[i] != 0 :
        for j in range(count[i]) :
            print(i)

