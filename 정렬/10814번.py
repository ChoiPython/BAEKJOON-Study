'''
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

'''

# n = int(input())

# sort = []
# bfage = -1
# for i in range(n) :
#     age, name = input().split()
#     age = int(age)

#     if bfage > age :
#         count = -1

#         while True :
#             try :
#                 if sort[count-1][0] > age :
#                     count -= 1
                
#                 else:
#                     sort.insert(count, [age, name])
#                     break
            
#             except:
#                 sort.insert(count, [age, name])
#                 break

    
#     else:
#         sort.append([age, name])

#     bfage = sort[-1][0]

# for i in range(len(sort)) :
#     print(sort[i][0], sort[i][1])


n = int(input())

sort = []
bfage = -1
for i in range(n) :
    age, name = input().split()
    age = int(age)
    sort.append([age, name])

# 정렬에 대해 배움 - 파이썬은 기본적으로 안정정렬인점.
# 정렬 시 key를 lambda식을 이용하여 age를 타겟팅 할 수 있었다.
sort.sort(key = lambda x : x[0])

for i in range(len(sort)) :
    print(sort[i][0], sort[i][1])
    





