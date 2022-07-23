'''서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?'''

'''인터넷 참고 1부터 N까지 수를 더하고 주어진 S의 값을 초과했을 때 마지막 이전의 수를 조정하여 S를 만들 수 있다.
    이때 N의 개수를 샌다.'''


S = int(input())

sum_data = 0

for i in range(1, S+1) :
    sum_data += i
    if sum_data > S :
        print(i-1)
        break

    elif sum_data == S :
        print(i)
        break
        
    