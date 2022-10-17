'''

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

'''

n = int(input())

num = list(map(int, input().split()))
out = 0


for i in range(len(num)) :
    check = True
    if num[i] == 1 :
        continue

    else:    
        for j in range(2, num[i]) :
            if num[i] % j == 0 :
                check = False
                break

        if check == True:
            out += 1

print(out)


# for i in num :  # 2 ~ N+1
#     if i == 1 :
#         continue

#     for j in range(2, int(i**0.5) + 1) :
#         if i % j == 0:
#             break

#     else:
#         print(i)








