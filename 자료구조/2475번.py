n = list(map(int, input().split()))

out = 0

for i in n :
    out += i**2

print(out % 10)
