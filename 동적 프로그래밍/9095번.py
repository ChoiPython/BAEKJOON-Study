
import sys

t = int(sys.stdin.readline())

for i in range(t):
    dp = [1, 2, 4]
    n = int(sys.stdin.readline())
    
    if n > 3:
        for j in range(3, n):
            dp.append(dp[j-1] + dp[j-2] + dp[j-3])        

        print(dp[-1])
    else: print(dp[n-1])





