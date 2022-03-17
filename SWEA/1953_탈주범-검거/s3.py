# 1953_탈주범-검거 풀이
# 2022-03-16

import sys
sys.stdin = open('sample_input.txt', 'r')


def delta(num):
    if num == 1:
        return [(0, 1), (1, 0), (0, -1), (-1, 0)]
    elif num == 2:
        return [(1, 0), (-1, 0)]
    elif num == 3:
        return [(0, 1), (0, -1)]
    elif num == 4:
        return [(0, 1), (-1, 0)]
    elif num == 5:
        return [(1, 0), (0, 1)]
    elif num == 6:
        return [(0, -1), (1, 0)]
    elif num == 7:
        return [(0, -1), (-1, 0)]
    return []


def bfs(v):
    global underground
    global result
    global L

    front = -1
    rear = 0
    queue = [[0] for _ in range(L+1)]
    queue[0] = [v]
    cnt = 1

    while front != rear:
        front += 1
        starts = queue[front]
        cnt += 1
        val = list()

        for start in starts:
            si = start[0]
            sj = start[1]

            if underground[si][sj] == 0:
                continue

            delta_v = delta(underground[si][sj])

            for di, dj in delta_v:
                ci = si + di
                cj = sj + dj

                # 파이프 번호로 찾기
                if 0 <= ci < N and 0 <= cj < M and visit[ci][cj] == 0:
                    if (di, dj) == (0, 1) and underground[ci][cj] in (1, 3, 6, 7):
                        result += 1
                        visit[ci][cj] = 1
                        val.append((ci, cj))

                    if (di, dj) == (1, 0) and underground[ci][cj] in (1, 2, 4, 7):
                        result += 1
                        visit[ci][cj] = 1
                        val.append((ci, cj))

                    if (di, dj) == (0, -1) and underground[ci][cj] in (1, 3, 4, 5):
                        result += 1
                        visit[ci][cj] = 1
                        val.append((ci, cj))

                    if (di, dj) == (-1, 0) and underground[ci][cj] in (1, 2, 5, 6):
                        result += 1
                        visit[ci][cj] = 1
                        val.append((ci, cj))

        if cnt == L:
            print('#{} {}'.format(tc, result))
            return

        rear += 1
        queue[rear] = val


T = int(input())
for tc in range(1, T+1):
    # N: 세로크기, M: 가로크기, R: 맨홀세로위치, C: 맨홀가로위치, L: 소요된 시간
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    result = 0
    bfs((R, C))