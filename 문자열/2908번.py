n = list(map(str, input().split()))
a = list(map(int, n[0]))
b = list(map(int, n[1]))
a = 100 * a[2] + 10 * a[1] + a[0]
b = 100 * b[2] + 10 * b[1] + b[0]

if a > b :
    print(a)
else:
    print(b)


