'''
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
'''

while True:

    string = list(map(str, input()))
    bigcount = []
    smallcount = []
    success = 1

    if len(string) == 1 and string[0] == '.' :
        break

    for i in range(len(string)) :
        if string[i] == '(' :
            smallcount.append(i)
            

        elif string[i] == ')' :
            if len(smallcount) != 0 and string[smallcount[-1]] == '(' :
                smallcount.pop(-1)

        elif string[i] == '[' :
            bigcount.append(i)
            

        elif string[i] == ']' :
            if len(bigcount) != 0 and string[bigcount[-1]] =='[' :
                bigcount.pop(-1)
                
            # 실패
            else :
                success = 0

    if len(bigcount) != 0 or len(smallcount) != 0 :
        success = 0

    if success == 1:
        print('yes')

    else :
        print('no')
