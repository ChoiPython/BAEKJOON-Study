''' 시간복잡도 N^2'''
# import sys

# n = int(sys.stdin.readline())

# heap = []
# out = []
# for i in range(n):
#     x = int(sys.stdin.readline())

#     if x == 0:  # print min
#         if len(heap) == 0 :      # empty list
#             out.append(0)
            
#         else:                   
#             out.append(heap.pop(heap.index(min(heap))))

#     else:       # insert x
#         heap.append(x)

# for j in out:
#     print(j)



''' 힙을 구현할 필욘 없는건가?.. '''
import sys
import heapq  # import heapq

n = int(sys.stdin.readline())
heap = []  

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if not heap:    # empty heap
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)



