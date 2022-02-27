# 11315_오목판정 풀이
# 2022-02-27

import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 오목판 크기 N*N
    rock = [list(map(str, input())) for _ in range(N)]
    stop = 0

    for i in range(N):
        for j in range(N):
            # o이 있을때, 델타 탐색으로 5개까지 본다 !
            if rock[i][j] == 'o':
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
                    cnt = 1
                    for p in range(1, 6):
                        if 0 <= i + di*p < N and 0 <= j + dj*p < N and rock[i+di*p][j+dj*p] == 'o':
                            cnt += 1
                        else:
                            break

                    if cnt == 5:
                        stop = 1
                        print('#{} YES'.format(tc))
                        break
                if stop == 1:
                    break
            if stop == 1:
                break
        if stop == 1:
            break

    if stop == 0:
        print('#{} NO'.format(tc))

