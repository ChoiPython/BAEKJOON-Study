'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

'''

# main 알고리즘 인터넷 참고  https://bambbang00.tistory.com/43
n, m = map(int ,input().split())
        
board = []
out = []

for i in range(n) : # 보드 입력(추가)
    board.append(input())  

# 8x8로 자르기 때문에 range -7
for a in range(n - 7) :
    for b in range(m - 7) :
        # 시작 B, W일 경우를 위한 변수
        caseW = 0
        caseB = 0
        for i in range(a, a + 8) :  # 잘라진 보드 전체 검사
            for j in range(b, b + 8):
                # 행(i) + 열(j)의 합이 짝수일 경우 시작 색과 같아야함 짝수는 달라야 함(핵심)
                if (i + j) % 2 == 0 :   
                    if board[i][j] != 'W':
                        caseW += 1

                    if board[i][j] != 'B':
                        caseB +=1

                else: 
                    if board[i][j] != 'B':
                        caseW += 1
                    if board[i][j] != 'W':
                        caseB += 1
        out.append(min(caseW, caseB))

print(min(out))

                    
                
            







