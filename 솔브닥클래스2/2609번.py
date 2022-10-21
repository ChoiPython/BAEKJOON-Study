'''
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
'''

n, m = map(int, input().split())
n1= n
m1 = m
# 최대공약수
if n1 > m1:
    # 유클리드 호제법
    while m1 != 0 :
        r = n1 % m1
        n1 = m1
        m1 = r

    gcd = n1

elif m1 > n1:
    # 유클리드 호제법
    while n1 != 0 :
        r = m1 % n1
        m1 = n1
        n1 = r

    gcd = m1

else:
    gec = n1

print(gcd)

# 최소공배수
lcm = n * m // gcd
print(lcm)

'''
math 사용
'''

