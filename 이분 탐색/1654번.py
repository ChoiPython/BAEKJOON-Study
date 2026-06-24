'''

오영식은 자체적으로 K개의 랜선을 가지고 있다. (랜선은 길이가 제각각이다. )

박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 

예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)

편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 

기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 

그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. 

N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 

이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

'''
# 논리 설계
# a = 2541
# maxv = 2541 // 11 # 231

# while True :
#     if 802 // maxv + 743 // maxv + 457 // maxv + 539 // maxv >= 11:
#         out = maxv
#         break

#     maxv -= 1

# print(out)


k, n = map(int, input().split())

lan = []

for i in range(k) :     # 길이 입력
    lan.append(int(input()))



# sumv = 0
# maxv = sum(lan) // n

# while True :
        
#     for i in lan :
#         sumv += i // maxv

#     if sumv >= n :
#         out = maxv
#         break

#     maxv -= 1
#     sumv = 0

# print(out)

# 이진탐색 알고리즘 
# 시작과 끝 범위(1 ~ 젤 긴 랜선)를 활용하여 중간값을 기준으로 분리하여 절반은 판단하지 않아도 됨



start = 1
end = max(lan) 

while start <= end:
    mid = (start + end) // 2
    lines = 0

    for i in lan:
        lines += i // mid

    if lines >= n :
        start = mid + 1

    else:
        end = mid - 1

print(end)




