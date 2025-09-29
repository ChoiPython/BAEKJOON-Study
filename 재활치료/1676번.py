'''
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 
구하는 프로그램을 작성하시오.
'''

n = int(input())    # 입력받기

# count = list()   # 리스트 선언
m = 1

for i in range(1, n+1) :    # 펙토리얼 계산
    m = m*i

count = str(m).split('0')   

print(count.count(''))








