'''
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
'''

# 
# stack = []
# string = ''
# while True:
#     string = input()
#     box = []

#     if string == '.' :
#         break
    
#     check = 0

#     # 열기, 닫기 개수는 맞지만 매칭되는 괄호 오류는 해결x
#     for i in range(len(string)) :
#         # 대괄호 추가
#         if string[i] == '[' :
#             box.append('[')
#             check += 1
        
#         # 대괄호 닫기
#         elif string[i] == ']' :
#             try :

#                 if box[check - 1] == '[' :
#                     check -= 1
#                     box.pop(-1)
                
#                 else :
#                     box.append('false') 
                    
#             except :
#                 box.append('false')
#                 break

#         # 소괄호 추가
#         if string[i] == '(' :
#             box.append('(')
#             check += 1

#         # 소괄호 닫기
#         elif string[i] == ')' :
#             try :
#                 if box[check - 1] == '(' :
#                     check -= 1
#                     box.pop(-1)
                    
#                 else:
#                     box.append('false')

#             except :
#                 box.append('false')
    
#     if len(box) == 0 :
#         print('yes')

#     else :
#         print('no')


string = ''

while True :
    string = input()
    stack = []

    check = -1       # 0 = 소괄호 / 1 = 대괄호

    if string == '.' :
        break

    count = 0

    for i in string :
        if i in ['(', ')', '[', ']'] :

            if i == '(' or i == '[' :
                stack.append(i)

            try :
                if i == ')' :
                    if stack[-1] == '(' :
                        stack.pop(-1)
                    
                    else:
                        stack.append('false')

                elif i == ']' :
                    if stack[-1] == '[' : 
                        stack.pop(-1)
                    
                    else:
                        stack.append('false')
            except :
                stack.append('false')

    if len(stack) == 0 :
        print('yes')

    else :
        print('no')



