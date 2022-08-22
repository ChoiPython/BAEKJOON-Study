from string import ascii_uppercase

n = input()

n = list(map(str, n.upper()))

num = [0 for i in range(26)]

out = list(map(str, ascii_uppercase))

for i in n :
    if i == 'A':
        num[0] += 1

    if i == 'B':
        num[1] += 1

    if i == 'C':
        num[2] += 1

    if i == 'D':
        num[3] += 1

    if i == 'E':
        num[4] += 1

    if i == 'F':
        num[5] += 1

    if i == 'G':
        num[6] += 1

    if i == 'H':
        num[7] += 1

    if i == 'I':
        num[8] += 1

    if i == 'J':
        num[9] += 1

    if i == 'K':
        num[10] += 1

    if i == 'L':
        num[11] += 1

    if i == 'M':
        num[12] += 1

    if i == 'N':
        num[13] += 1

    if i == 'O':
        num[14] += 1

    if i == 'P':
        num[15] += 1

    if i == 'Q':
        num[16] += 1

    if i == 'R':
        num[17] += 1 

    if i == 'S':
        num[18] += 1

    if i == 'T':
        num[19] += 1
    
    if i == 'U':
        num[20] += 1

    if i == 'V':
        num[21] += 1

    if i == 'W':
        num[22] += 1

    if i == 'X':
        num[23] += 1

    if i == 'Y':
        num[24] += 1

    if i == 'Z':
        num[25] += 1

count = 0
for i in num :
    if i == max(num) :
        count += 1


if count > 1 :
    print('?')

else:
    print(out[num.index(max(num))])
    












