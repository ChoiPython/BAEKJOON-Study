"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
"""



# 1. w,b의 갯수가 제일 많은 상황
# 2. 번갈아 가면서 체크 하다가 같은 거면 카운트
#    ㄴ 칠해야 하는 정사각형의 개수
# 3. 최솟값을 어떻게 찾지?
# 4. 8x8을 쪼갤 수 있는 모든 경우의 수를 다 세본다?
# ㄴ 효율적인가? 하지만 확실한 방법
# 5. 입력 받으면서 확인하기? 가능한가?
# 6. 근데 입력을 어떻게 받아야할까?
#    ㄴ numpy를 써야하나?..


import numpy as np
n, m = map(int, input().split())    # mxn 모양
matrix = np.zeros(n*m, dtype=str).reshape(m,n) # m,n 빈행렬 만들기


'''  넘파이로 저장
import numpy as np
a = np.zeros(64, dtype=str).reshape(8,8)

print(a[0])
data = list(map(str, input().split()))
data[0] = list(data[0])
print(data)
for i in range(8):
    a[0][i] = data[0][i]
print(a[0])
'''
'''  리스트로 저장
a = [[]]
data = list(map(str, input().split()))
data[0] = list(data[0])
print(data[0])
a[0] = (data[0])

print(a)

'''


for i in range(m):  # 행
    data = list(map(str, input().split()))  # WB입력
    data[0] = list(data[0])                 # 문자열 분리 'W','B','W'...
    matrix[i] = data[0]
    print(matrix)

    # for j in range(n):  # 열
        # pass












