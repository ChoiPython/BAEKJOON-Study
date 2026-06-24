'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라
정렬하는 프로그램을 작성하시오.
    1. 길이가 짧은 것부터
    2. 길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.
'''

N = int(input())    # 단어개수
voca = list()       # 저장할 리스트 생성)

for i in range(N) :
    eng = input()   # 단어
    num = 0 # 리스트 탐색 매개변수
    if len(voca) == 0 : # 리스트가 비어 있을 경우
        voca.append(eng)    
        pass

    else:   # 나머지 경우
        if eng in voca : # 이미 존재할 경우 넘어감
            pass

        else:
            while len(voca[num]) < len(eng) :    # 길이 수 
                num += 1        # 다음 걸로 탐색
                if num == len(voca) :   # 마지막까지 간 경우 탐색 종료
                    break
                
            if num == len(voca) :   # 마지막까지 간 경우 탐색 종료
                pass
            else:
                # 사전 순 비교 길이 수 같음.
                while voca[num] < eng and len(voca[num]) == len(eng) :     
                    num += 1
                    if num == len(voca) :   # 마지막까지 간 경우 탐색 종료
                        break

            voca.insert(num, eng)   # 단어 저장

for ans in voca:
    print(ans)



