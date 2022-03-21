# 5688_세제곱근을-찾아라 풀이
# 2022-03-21
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = -1

    # 1부터 세제곱해서 구하기
    N = N**(1/3)
    print(N)
    if N-int(N) == 0:
        result = int(N)

    print('#{} {}'.format(tc, result))
