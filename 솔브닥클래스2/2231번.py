'''
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

'''

n = int(input())
result = 0

for i in range(1, n+1) :
    num = list(map(int, str(i)))

    result = i + sum(num)
    
    if result == n:
        print(i)
        break
    if i == n:
        print(0)