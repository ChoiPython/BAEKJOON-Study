'''

1. 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인한다
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치한다
    else 그냥 인쇄

    result - 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

'''

# 중요도 비교 후 뒤로 보내기
def Reback(que) :
    que.append(que.pop(0))
    return que

# 테스트케이스 개수
case = int(input())

out = []

for i in range(case) :
    # n : 개수 / m : 위치
    n, m = map(int, input().split())
    
    # 중요도 : 중복O
    pos = list(map(int, input().split()))
    
    # pos 인덱스 조작 
    pos_index = [a for a in range(n)]

    # 리스트 인덱스 조작
    index = pos[0]
    outv = 0    # 출력 순서

    while True :
        if index < max(pos) :
            pos, pos_index = Reback(pos), Reback(pos_index)
            index = pos[0]

        elif index == max(pos) :
            # index가 가장 크다면 pop
            pos.pop(0)
            pos_pop = pos_index.pop(0)
            outv += 1

            # m과 고유 인덱스가 같을 경우
            if m == pos_pop :
                out.append(outv)
                break

            # index 초기화
            index = pos[0] 
        
for i in out :
    print(i)

        


    
        

        


        

    


    








