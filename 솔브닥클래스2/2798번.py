'''

제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 
플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.


'''

n, m = map(int, input().split())
num = list(map(int, input().split()))

black = 0
com = []

num.sort()
for i in range(len(num)) :
    for j in range(i+1, len(num)) :
        for k in range(j+1, len(num)) :
            black = num[i] + num[j] + num[k]
            
            if black == m :
                print(black)
                exit()
                
                

            elif black < m :
                com.append(black)


print(max(com))


                




    




