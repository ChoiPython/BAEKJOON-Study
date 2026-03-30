n, m = map(int, input().split())

poketmonlist = []
poketmondict = dict()
for i in range(n):
    name = input()
    poketmonlist.append([name, i+1])
    poketmondict[name] = i+1


for j in range(m):
    find = input()
    if find.isdigit() :
        print(poketmonlist[int(find)-1][0])
    
    else:
        print(poketmondict[find])

