# 5250_최소-비용 풀이
# 2022-04-09

import sys
sys.stdin = open('sample_input.txt', 'r')


def bfs(i, j):
    front = -1
    rear = 0
    queue = [(i, j)]
    distances[i][j] = 0      # 시작위치 거리 = 0

    while front < rear:
        front += 1
        si, sj = queue[front]

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):      # 델타 탐색
            ni = si + di
            nj = sj + dj

            if 0 <= ni < N and 0 <= nj < N:    # 인덱스 범위내에 있으면
                dis = 1      # 기본 연료 소비량 = 1

                # 더 높은 곳으로 이동할 때는 높이차만큼 연료가 더 소비됨
                if arr[ni][nj] > arr[si][sj]:
                    dis += arr[ni][nj] - arr[si][sj]

                # 저장된 연료소비량보다 이동시 연료소비량이 더 작을 때
                if distances[ni][nj] > distances[si][sj] + dis:
                    distances[ni][nj] = distances[si][sj] + dis
                    queue.append((ni, nj))
                    rear += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distances = [[999999999999] * N for _ in range(N)]

    bfs(0, 0)
    print('#{} {}'.format(tc, distances[N - 1][N - 1]))

