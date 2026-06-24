out = []

while True:
    try:
        a, b = map(int, input().split())
        out.append(a + b)

    except:
        break

for j in range(len(out)):
    print(out[j])

