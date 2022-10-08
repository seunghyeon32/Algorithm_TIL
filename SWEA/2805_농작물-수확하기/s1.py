# 2805_농작물 수확하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = 0
    arr = [list(map(int, input())) for _ in range(N)]
    middle = N//2

    # 가장 가운데 가로 더하기
    result += sum(arr[middle])

    # 가운데 가로행을 기준으로 대칭되는 부분의 가치 모두 더하기
    for n in range(middle):
        result += arr[n][middle] + arr[N-n-1][middle]
        for m in range(1, n+1):
            result += arr[n][middle+m] + arr[n][middle-m] + arr[N-n-1][middle+m] + arr[N-n-1][middle-m]

    print(f'#{tc} {result}')