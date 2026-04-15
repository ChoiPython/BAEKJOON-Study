# Let's go DP

'''
case1: 1
case2: 2
case3: 3
case4: 5
case5: 8
...
case(n): case (n-1) + case (n-2)
'''

import sys

n = int(sys.stdin.readline())

dp = [1, 2]

for i in range(n):
    if i == 0 or i == 1:
        pass

    else:
        dp.append(dp[i-1] + dp[i-2])
        # print("check:{} {} ".format(i, dp[i-1] + dp[i-2]))

if n>2:
    print(dp[-1] % 10007)

else:
    print(n)


