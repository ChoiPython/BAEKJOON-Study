'''

김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

'''

n, m = map(int, input().split())
hset = set()
for i in range(n):
    hear = input()
    hset.add(hear)

sset = set()
for j in range(m): 
    see = input()
    sset.add(see)
outset = hset&sset
print(len(hset & sset)) # 인원수

# 명단
out = []
for k in outset:
    out.append(k)
out.sort()
for l in out:
    print(l)






