h, m = map(int, input().split())

h = 60 * h
total = h + m - 45

h = total // 60
m = (total - h * 60) 
if h < 0 :
    h = 24 + h
print(h, m)






