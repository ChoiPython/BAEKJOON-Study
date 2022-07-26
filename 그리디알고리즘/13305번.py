'''각 도시의 주유소를 걸치고 도로를 지나 마지막 도시로 도착했을 때 기름비용을 최저로 쓰기'''

n = int(input())

road = [i for i in map(int, input().split())]
oil =  [i for i in map(int, input().split())]

all = oil[0] * road[0]
data = oil[0]

for i in range(1, n-1) :
    
    if data > oil[i] :

        data = oil[i]

    all += data * road[i]

print(all)











