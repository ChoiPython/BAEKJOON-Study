
test = int(input())

for i in range(test):
    out = [[1,0], [0,1]]
    num = int(input())
    if num == 0:
        print(1, 0)
        continue
    elif num == 1:
        print(0, 1)
        continue
    else:
        for j in range(num+1):
            if j > 1 :
                cnt0 = 0
                cnt1 = 0
                cnt0 += out[j-1][0] + out[j-2][0]
                cnt1 += out[j-1][1] + out[j-2][1]
                out.append([cnt0, cnt1])
            
        print(out[-1][0], out[-1][1])