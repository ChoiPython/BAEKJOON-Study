'''

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

'''

import sys

n = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for i in range(n)]

# 산술평균
n_sum = sum(num)
print(int(round(n_sum / n)))

# 중앙값
n_sort = sorted(num)
print(n_sort[n // 2])

# 최빈값
max_most = -1
n_most = num.copy()
same = [0]

for i in range(len(num)) :
    most = 0
    # 각 숫자 개수 세기
    while num[i] in n_most:
        most += 1
        n_most.remove(num[i])

    if max_most < most :
        max_most = most
        most_num = num[i]   # 해당 숫자 저장
        # same에 2개 이상 있을 경우
        if len(same) > 1 :
            same.clear()
            same.append(0)

        same[-1] = num[i]

    elif max_most == most :
        same.append(num[i])
        same.sort()
        most_num = same[1]
        

print(most_num)
        

# 범위
print(max(num) - min(num))
    
        
    

            
    


