# 10726_이진수-표현 풀이
# 2022-03-24
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 'ON'

    # 뒤에서 N번째 비트들만 확인
    for _ in range(N):
        if M%2:
            M = M//2
            continue
        else:
            # 하나라도 꺼져있으면 결과는 OFF
            result = 'OFF'
            break

    print('#{} {}'.format(tc, result))