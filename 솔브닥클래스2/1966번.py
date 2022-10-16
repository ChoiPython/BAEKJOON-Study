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
    
    # 문서 중요도
    doc = pos[m] 

    # 리스트 인덱스 조작
    index = pos[0]
    count = 0
    outv = 0     # 출력 순서
    popv = 0

    while True:
        try:
            # 중요도 높은 것 발견
            if index < max(pos) :        
                pos= Reback(pos)
                # index 재지정
                index = pos[0]

            # 조건에 맞는 출력 상황
            elif doc == pos[0] and m == count + popv :
                out.append(outv + 1)
                break

            elif index == max(pos) and count == popv :
                pos.pop(0)
                count = 1 + popv
                popv += 1
                index = pos[0]
                outv += 1
                continue

            # 다른 
            else:
                pos.pop(0)
                index = pos[0]
                outv += 1
                
            
            count += 1

            # 한 바퀴 진행 후 초기화
            if count >= n :
                count = 0
                n -= 1
        except:
            # out.append(outv + 1)
            break

for i in out :
    print(i)

        


    
        

        


        

    


    








