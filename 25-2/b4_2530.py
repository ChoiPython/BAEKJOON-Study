'''
인공지능 시계
훈제오리구이를 시작하는 시각과 
오븐구이를 하는 데 필요한 시간이 초 단위로 주어졌을 때,
오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오
'''
A, B, C = input().split()
cook = int(input())
A = int(A) * 3600
B = int(B) * 60
C = int(C)

result = A + B + C + cook


while result >= 86400:
    result -= 86400

hours = result // 3600
result -= hours * 3600
min = result // 60
result -= min * 60
sec = result
print(hours, min, sec)





