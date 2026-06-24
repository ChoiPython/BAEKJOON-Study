n = int(input()) 

weight = []
height = []
box = []
scoor = [1 for i in range(n)]

# 몸무게, 키 입력
for i in range(n) :
    w, h = map(int, input().split()) 
    weight.append(w)
    height.append(h)
    box.append([w, h])

for i in range(n) :
    weightval = box[i][0]
    heightval = box[i][1]
    for j in range(n) :
        if weightval < weight[j] and heightval < height[j] :
            scoor[i] += 1
            pass

    print(scoor[i], end=' ')



