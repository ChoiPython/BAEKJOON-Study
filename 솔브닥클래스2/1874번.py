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
push_list = [1]

# 실패 확인 변수
false = True

# 결과 리스트
out = []
start = 1       # push 시작 벨류
index = 0       # num 인덱스 추출

for i in range(len(num)) :
    # push
    while start <= num[i]:
        push_list.append(start)
        out.append('+')
        start += 1

    # pop -> stack 구조상 마지막 pop
    pp = push_list.pop(-1)

    # pp와 num[i]이 다를경우
    if pp != num[i] :
        false = False
        print('NO')
        break

    # pp와 num[i]가 같을 경우 - 정상
    else:
        out.append('-')
        
if false == True:
    for i in out :
        print(i)









