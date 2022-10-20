'''

제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

'''

def deque(num, stop) :
    if stop:
        num.pop(0)
        return num

    else:
        num.pop(0)
        push = num.pop(0)
        num.append(push)
        return num

n = int(input())

num = [a for a in range(1, n + 1)]
stop = False
count = 1 # n // 2 + 1

while True:
    if n < 3:
        print(n)
        exit()

    if stop == True:
        break

    else:
        if count == n - 1:
            stop = True
            deque(num, stop)

        else:   
            num = deque(num, stop)

        count += 1

print(num[0])


