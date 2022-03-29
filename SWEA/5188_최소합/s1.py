# 5188_최소합
# 2022-03-29

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 0행, 0열 누적합 구하기
    for i in range(1, N):
        arr[0][i] += arr[0][i-1]
        arr[i][0] += arr[i-1][0]

    # 각 좌표의 누적합을 구한다.
    # 단, 위와 왼쪽 값 중 작은 값을 더한다.
    for n in range(1, N):
        for m in range(1, N):
            arr[n][m] += min(arr[n][m-1], arr[n-1][m])

    print('#{} {}'.format(tc, arr[N-1][N-1]))
