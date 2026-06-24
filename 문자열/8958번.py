from re import S


n = int(input())
out = []

for i in range(n) :
    pass
    s = input().split('X')

    while '' in s :
        s.remove('')

    count = 0

    for j in range(len(s)) :
        a = len(s[j])
        count += a * (a + 1) / 2
    out.append(int(count))

for l in range(len(out)):
    print(out[l])





