import numpy as np

h, w = map(int, input().split())

a = np.empty((0,1))

for i in range(h):
    board = input()
    a = np.append(a, np.array([[board]]), axis=0)

count_row = [0 for s in range(h - 7)]
count_col = [0 for s in range(h - 7)]

for i in range(h - 7) :
    data = list(map(str, a[i][0]))
    com_data = data[0]

    for j in range(1, len(data)):
        if com_data == data[j] :
            count_col[i] += 1

        else: 
            count_row[i] += 1
        com_data = data[j]

max_row = count_row.index(max(count_row))
start_col = count_col[count_row.index(max(count_row))]

if w - start_col - 1 < 8 :
    start_col -= 8 - (w -start_col - 1)

# list(map(str, a[max_row : max_row + 8][0][0]))[start_col: start_col + 8] 인덱싱 
for j in range(8):
    choice_board = list(map(str,a[max_row : max_row + 8][j][0]))[start_col: start_col + 8]
    print(choice_board)






            
    


















