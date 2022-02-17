# 1954_달팽이숫자_활용 풀이
# 2022-02-14

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = [n for n in range(1, N*N+1)]    # 1 ~ (N^2) 숫자 생성
    arr = [[0] * N for _ in range(N)]   # 배열 생성
    arr_1 = list()                      # 1차원 배열

    # 1차원 배열 만들기
    for num in nums:
        arr_1.append(num)

    # 달팽이로 집어넣자 !
    dr = [1, 0, -1, 0]    # 하 우 상 좌 (행)
    dc = [0, -1, 0, 1]    # 하 우 상 좌 (열)
    direction = 0
    cc = N-1
    cr = 0

    # 5 4 4 3 3 2 2 1 1
    for k in range(N, 0, -1):
        if k == N:
            for p in range(N):
                arr[0][p] = arr_1.pop(0)
            continue

        # 4 3 2 1 은 2번씩 !
        a = 0
        while a < 2:
            # 4 3 2 1
            for q in range(k):
                cc += dc[direction]
                cr += dr[direction]
                arr[cr][cc] = arr_1.pop(0)

            # 위치 변수 초기화
            if direction == 3:
                direction = 0
            else:
                direction += 1

            a += 1

    print('#{}'.format(tc))

    for i in range(N):
        for j in range(N-1):
            print('{} '.format(arr[i][j]), end='')
        print(arr[i][N-1])
