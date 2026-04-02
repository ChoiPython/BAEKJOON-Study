'''
입력의 첫째 줄에 계단의 개수가 주어진다.

둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 
계단에 쓰여 있는 점수는 10,000이하의 자연수이다.
'''


stairs = int(input())

score = []
out = []
for i in range(stairs):
    n = int(input())
    score.append(n)
    if i == 0 :
        out.append(score[0])

    elif i == 1:
        out.append(score[0]+score[1])
    
    elif i == 2:
        out.append(max((score[0]+score[2]), (score[1] + score[2])))

    else:
        out.append(max((out[i-2]+score[-1]), (out[i-3]+score[-2]+score[-1])))
        
print(out[-1])



    
    


