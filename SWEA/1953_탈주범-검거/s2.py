# 1953_탈주범-검거 풀이
# 2022-03-16

import sys
sys.stdin = open('sample_input.txt', 'r')


def right(i, j):
    global underground
    global val
    global result

    if 0 <= i < N and 0 <= j + 1 < M:
        if underground[i][j + 1] in (1, 3, 6, 7) and not visit[i][j+1]:
            result += 1
            visit[i][j+1] = 1
            val.append([i, j+1])
            return


def bottom(i, j):
    global underground
    global val
    global result
    if 0 <= i + 1 < N and 0 <= j < M:
        if underground[i + 1][j] in (1, 2, 4, 7) and not visit[i+1][j]:
            result += 1
            visit[i+1][j] = 1
            val.append([i+1, j])
            return


def left(i, j):
    global underground
    global val
    global result

    if 0 <= i < N and 0 <= j-1 < M:
        if underground[i][j-1] in (1, 3, 4, 5) and not visit[i][j-1]:
            result += 1
            visit[i][j-1] = 1
            val.append([i, j-1])
            return


def top(i, j):
    global underground
    global val
    global result

    if 0 <= i-1 < N and 0 <= j < M:
        if underground[i-1][j] in (1, 2, 5, 6) and not visit[i-1][j]:
            result += 1
            visit[i-1][j] = 1
            val.append([i-1, j])
            return


def bfs(v):
    global underground
    global result
    global val

    front = 0
    rear = 0
    queue = [[0] for _ in range(L+1)]
    queue[front] = [v]
    cnt = 1

    while queue:
        starts = queue[front]
        front += 1
        cnt += 1
        for start in starts:
            si = start[0]
            sj = start[1]

            if underground[si][sj] == 0:
                continue
            elif underground[si][sj] == 1:
                right(si, sj)
                bottom(si, sj)
                left(si, sj)
                top(si, sj)
                continue
            elif underground[si][sj] == 2:
                top(si, sj)
                bottom(si, sj)
                continue
            elif underground[si][sj] == 3:
                right(si, sj)
                left(si, sj)
                continue
            elif underground[si][sj] == 4:
                top(si, sj)
                right(si, sj)
                continue
            elif underground[si][sj] == 5:
                bottom(si, sj)
                right(si, sj)
                continue
            elif underground[si][sj] == 6:
                left(si, sj)
                bottom(si, sj)
                continue
            elif underground[si][sj] == 7:
                top(si, sj)
                left(si, sj)
                continue

        if cnt == L:
            print('#{} {}'.format(tc, result))
            return

        rear += 1
        queue[rear] = val
        val = list()


T = int(input())
for tc in range(1, T+1):
    # N: 세로크기, M: 가로크기, R: 맨홀세로위치, C: 맨홀가로위치, L: 소요된 시간
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    result = 0
    val = list()
    bfs([R, C])