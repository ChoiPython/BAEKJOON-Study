'''

제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

'''

def Reback(num) :
    num.append(num.pop(0))
    return num

def Throw(num) :
    num.pop(0)
    return num

n = int(input())

num = [a for a in range(1, n + 1)]
index = 0
while len(num) != 1:
    num = Throw(num)
    print(num)

    print(num)
    num = Reback(num)
    print()
    
print(num[0])
