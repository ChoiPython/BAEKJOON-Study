# 메모리가 4MB밖에 주어지지 않았다.
# 비트마스크란 무엇인가?

import sys
input = sys.stdin.readline

S = 0  # 20비트만 사용하는 비트마스크. 정수 하나로 숫자 20개 관리
M = int(input())

# 1 << k : 2진수로 1은 0...01이니까, << 왼쪽으로 k칸 비트를 밀면 k번째 비트가 켜진다.
for _ in range(M):
    # 한 줄씩 입력을 읽고 바로 처리하는 구조가 메모리 초과가 안 난다.
    parts = input().split()
    
    match parts[0]:
        case "add":
            # |는 or연산. 자리별로 계산해서 둘중하나가 1이면 1 둘다0이면 0    
            # 0b100 | 0b001 == 0b101. 꺼져있던게 켜짐
            S |= (1 << int(parts[1]) - 1)
        case "remove":
            # &는 and연산. 자리별로 계산해서 둘다1이면 1 아니면 0
            # ~는 not연산. 모든 비트 뒤집기
            # 0b101 & 0b110 == 0b100. 원래 1인건 그대로 1이고 끌것만 0됨
            S &= ~(1 << int(parts[1]) - 1)
        case "check":
            # S에 and연산으로 하나만 켜진 비트를 넣어 True면 1을 print 아니면 0
            # 비트를 출력하는 것보다 이게 더 효율적이다.
            print(1 if S & (1 << int(parts[1]) - 1) else 0)
        case "toggle":
            # ^는 xor연산. 자리별로 계산해서 같으면 0 다르면 1
            # 0b101 ^ 0b001 == 0b100. 기존 자리에 ^0이 된다 해서 변화가 없다.
            S ^= (1 << int(parts[1]) - 1)
        case "all":
            # 21번 비트만 켜두고 거기서 1을 빼면 21이 꺼지고 1~20이 켜진다.
            S = (1 << 20) - 1
        case "empty":
            S = 0