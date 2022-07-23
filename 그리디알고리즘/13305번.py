'''각 도시의 주유소를 걸치고 도로를 지나 마지막 도시로 도착했을 때 기름비용을 최저로 쓰기'''

n = int(input())

road = [i for i in map(int, input().split())]       # km
oil = [j for j in map(int, input().split())]        # price

cost = 0

m_oil = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

for i in range(n-1) :
    com_data = 0

    k = 0
    for k in range(i) :
        com_data += oil[k] * road[k]
        k = k+1

    for j in range(n-i-1) :
        com_data += oil[i] * road[k:][j]

    if m_oil > com_data :
        m_oil = com_data

print(m_oil)











