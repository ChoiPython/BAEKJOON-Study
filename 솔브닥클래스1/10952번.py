out = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    out.append(a + b)

for i in range(len(out)):
    print(out[i])
    