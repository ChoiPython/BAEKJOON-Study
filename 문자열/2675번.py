n = int(input())

data = []

for i in range(n) :
    r, s = map(str, input().split())

    data.append([int(r), s])

for i in data :
    out = list(map(str, i[1]))      # 'A', 'B', 'C'
    for k in out :
        for l in range(i[0]) :
            print(k, end= '')
    print()
        

        



