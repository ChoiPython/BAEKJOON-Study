import sys

t = int(sys.stdin.readline())


for _ in range(t):
    clothes = []
    titles = dict()         # 'title': 개수
    out = 0
    n = int(sys.stdin.readline())
    for _ in range(n):  
        c, title = sys.stdin.readline().split()

        if title in titles:     # 종류 개수 count
            titles[title] += 1

        else: titles[title] = 1 # 없다면 추가하고 카운트 시작
    
        clothes.append(c)
    
    # 하나만 입는 경우
    val = 1
    idx = list(titles.keys())

    for i in range(len(titles)):
        val *= titles[idx[i]]+1
    
    out += val -1
    
    print(out)

    



