n = int(input())

for i in range(1, n + 1) :
    for j in range(n - i):
        print(' ', end='')
    for k in range(i) :
        print('*', end = '')
    print()

    
# for i in range(5) :
    
#     for j in range(5-i) :
#         print('*', end = '')
#     print()






