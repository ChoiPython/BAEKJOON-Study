'''
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 

스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 

이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 

임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 

있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 

이를 계산하는 프로그램을 작성하라.
'''

# No -> 출력 해야함
n = int(input())

# 수열 입력
num = [int(input()) for i in range(n)]

# 숫자 직접 넣어보면서 비교하기 위한 리스트
push_list = []

# 결과 리스트
out = []

start = 0       # push 시작 벨류
index = 0       # num 인덱스 추출
plus = 0        # num과 인덱스 맞추기 위한

while start <= n + 1:
    # 스텍 리스트가 공백일 경우
    if not push_list:
        push_list.append(start + 1)
        out.append('+')
        start += 1

    # push 
    elif push_list[-1] < num[index] :
        push_list.append(start + 1)
        out.append('+')
        # print("push : {}".format(push_list))
        # push 후 
        start += 1
        
    # pp에 저장하고 num[index]와 다르면 break후 NO 출력하자
    else:
        # NO 상황
        if push_list[-1] != num[index] :
            out.append('NO')
            break

        try:
            while push_list[-1] == num[index]:
                out.append('-')
                index += 1


        # push_lisf가 비워지거나 index가 num의 범위를 벗어낫을 때 종료
        except (IndexError):    
            # print("EXCEPT")
            out.append('NO')
            break


if 'NO' in out :
    print('NO')
    
else:
    for i in out :
        print(i)
    









