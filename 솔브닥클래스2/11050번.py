'''
이항계수 구하기
'''

import sys 
import math

n, k = map(int, sys.stdin.readline().split())

up = math.factorial(n)
down = math.factorial(n-k) * math.factorial(k)

print(int(up / down))