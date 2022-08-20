a = list(map(int, input().split()))

b = [i for i in range(1, 9)]
c = b[::-1]

if a == b :
    print('ascending')

elif a == c :
    print('descending')

else:
    print('mixed')




