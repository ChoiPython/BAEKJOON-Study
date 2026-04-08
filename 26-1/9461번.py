import sys

test = int(sys.stdin.readline())

for _ in range(test):
    dp = [1, 1, 1]
    n = int(sys.stdin.readline())
    if n == 1 :
        print(1)
    elif n == 2:
        print(1)

    elif n == 3:
        print(1)

    else:
        for i in range(4, n+1):
            dp.append(dp[(i-1)-2]+ dp[(i-1)-3])

        print(dp[-1])
