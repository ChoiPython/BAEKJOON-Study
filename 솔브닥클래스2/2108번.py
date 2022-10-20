'''

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

'''

import sys
from typing import Counter

n = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for i in range(n)]

# 산술평균
n_sum = sum(num)
print(int(round(n_sum / n)))

# 중앙값
n_sort = sorted(num)
print(n_sort[n // 2])

# 최빈값
n_most = num.copy()
most_num = 0 # output
# Counter().most_common() -> 최빈값을 (원소, 빈도수)상태 리스트로 바뀜
count = Counter(n_most).most_common()
# 개수가 2개 이상이며 최빈값이 2개이상일 때
if len(count) > 1 and count[0][1] == count[1][1] :

    index = 1
    while True:
        try:
            if count[0][1] > count[index][1] :
                count.remove(count[index])
            else:
                index += 1

        except (IndexError):
            break   
        
    count.sort()
    print(count[1][0])

else:
    print(count[0][0])

# 범위
print(max(num) - min(num))
    
        
    

            
    


