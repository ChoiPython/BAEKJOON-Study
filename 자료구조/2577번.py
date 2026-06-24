n = [int(input()) for i in range(3)]

a = str(n[0] * n[1] * n[2])


a = list(map(int, a))

count = [0 for i in range(10)]

for i in range(10) :
    while i in a :
        count[i] += 1
        a.remove(i)

for i in count :
    print(i)


