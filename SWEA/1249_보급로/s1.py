# 1249_보급로 풀이
# 2022-03-29

import sys
sys.stdin = open('input.txt', 'r')


def bfs(i, j):
    global arr
    global visited
    front = -1
    rear = 0
    queue = [[i, j]]
    visited[i][j] = 0

    while front < rear:
        front += 1
        si, sj = queue[front]

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = si + di
            nj = sj + dj

            # 갈 수 있는 가장 짧은 경로로 대체
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > arr[ni][nj] + visited[si][sj]:
                visited[ni][nj] = arr[ni][nj] + visited[si][sj]
                queue.append([ni, nj])
                rear += 1

    return print('#{} {}'.format(tc, visited[N - 1][N - 1]))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[99999999999999999] * N for _ in range(N)]
    bfs(0, 0)