# 1961_숫자배열회전 풀이
# 2022-02-18
import sys

sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T + 1):
    # N*N 배열의 크기
    # arr: 기준배열
    N = int(input())
    arr = list()
    arr_90 = [[0] * N for _ in range(N)]
    arr_180 = [[0] * N for _ in range(N)]
    arr_270 = [[0] * N for _ in range(N)]

    # 기준배열 만들기
    for n in range(N):
        arr.append(list(map(str, input().split())))

    # 90도 회전
    for i in range(N):
        for j in range(N):
            arr_90[j][N - i - 1] = arr[i][j]

    # 180도 회전
    for i in range(N):
        for j in range(N):
            arr_180[j][N - i - 1] = arr_90[i][j]

    # 270도 회전
    for i in range(N):
        for j in range(N):
            arr_270[j][N - i - 1] = arr_180[i][j]

    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(arr_90[i]), end=' ')
        print(''.join(arr_180[i]), end=' ')
        print(''.join(arr_270[i]))
