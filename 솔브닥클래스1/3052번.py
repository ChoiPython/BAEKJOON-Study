n = [int(input()) for i in range(10)]
a = set()

for i in range(len(n)) :
    a.add(n[i] % 42)
    
print(len(a))



