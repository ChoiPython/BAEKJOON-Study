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

stack_list = []
com = []
out = []
start = 1
plus = 0

def stack(start, num, com, out, stack_list) :
    returnValue = True
    # pop 
    try:
        for i in range(start, num + 1) :

                if num in com :
                    pass

                else:
                    com.append(i)

                # 단순히 푸시 팝만 하면 안됨 - 모든경우가 다 되버린다.
                if com[-1] > num :
                    returnValue = False
                    print("RetrunfValue = False")
                    break

                # push
                else:
                    print("push")
                    stack_list.append(i)
                    out.append('+')
                    print(stack_list)

        # pop
        if num in stack_list:
            print("pop")
            stack_list.remove(i)
            out.append('-')
            # pop시킨후 value 저장 -> No 경우체크 -> 배열이 다르면 NO
            com.pop(-1)
            print(stack_list)


    except Exception as e:
        print("except발생 : {}".format(e))
        returnValue = False
            
    return com, out, returnValue, stack_list

# 첫번째 숫자 만큼 push는 해줘야함 + pop 한개
# pop을 기준으로 세트 분리
for i in range(len(num)) :
    print("start = {}, num = {}, plus = {}".format(start, num[i], plus))
    if start <= num[i] :
        com, out, returnValue, stack_list = stack(start + plus, num[i], com, out, stack_list)
        start = num[i]

        if returnValue == False :
            break

    # start > num[i]
    else:
        try :
            if num[i] > num[i + 1]:
                com.pop(-1)
                out.append('-')
                plus += 1

        except(IndexError):
            pass
        
        except:
            returnValue = False

# NO 상황
if returnValue == False:
    print("NO")

else:
    for i in out :
        print(i)



# false - No에 대한 예외사항 일반화에 해당하지 않음
#  compare = -1
# for i in range(len(num)-1):
#     # 현재보다 다음값이 크고 그 다음값과 2의 차이가 난다면 No
#     try:
#         if compare < num[i] :
#             compare = num[i]
#             if compare > num[i+1] + 1 :
#                 print("NO")
#                 exit()

#     except(IndexError):
#         break




