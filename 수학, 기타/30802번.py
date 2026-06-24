import sys

n = int(sys.stdin.readline())

s, m, l, xl, xxl, xxxl = map(int, sys.stdin.readline().split())

t, p = map(int, sys.stdin.readline().split())

def div(size, t):
    cnt = 0
    if size == 0:
        return 0
    else:
        if size % t != 0:
            cnt += size // t + 1
            return cnt
        
        else:
            cnt += size // t
            return cnt

count = 0
count += div(s, t)
count += div(m, t)
count += div(l, t)
count += div(xl, t)
count += div(xxl, t)
count += div(xxxl, t)

print(count)
print(n//p, n-p*(n//p))













