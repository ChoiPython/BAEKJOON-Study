n = int(input())

grade = list(map(int, input().split()))
maxv = max(grade)

for i in range(len(grade)) :
    grade[i] = grade[i] / maxv * 100

print(sum(grade) / n)

