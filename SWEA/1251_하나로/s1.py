# 1251_하나로
# 2022-04-10

import sys
sys.stdin = open('input.txt', 'r')


def PRIM():
    global result

    s = 0    # 0번 섬에서 시작한다고 가정
    distances[s] = 0     # 0번섬에서 갈 수 있는 거리를 0으로 초기화

    for _ in range(N-1):
        visited[s] = True   # 방문처리

        # s번 섬에서 갈 수 있는 거리정보 저장
        for idx, d in G[s]:
            if not visited[idx] and distances[idx] > d:
                distances[idx] = d

        # 거리에 저장된 섬들 중 방문하지 않은 섬 중에
        # 가장 거리가 짧은 섬 찾기
        min_idx = -1
        min_val = 99999999999999999999
        for i in range(N):
            if not visited[i] and min_val > distances[i]:
                min_idx = i
                min_val = distances[i]

        # min_idx 섬으로 이동
        # result에 가중치 저장
        s = min_idx
        result += min_val


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    island_x = list(map(int, input().split()))      # 섬들의 x좌표
    island_y = list(map(int, input().split()))      # 섬들의 y좌표
    island = list(zip(island_x, island_y))          # (x,y)
    E = float(input())                              # E: 환경부담 세율
    G = [[] for _ in range(N)]                      # 그래프
    distances = [99999999999999999999] * N          # 최단 거리 저장
    visited = [0] * N                               # 방문여부표시
    result = 0                                      # 최소 신장 트리의 가중치 합

    # 섬들의 그래프 만들기
    # dis: 환경부담금
    for n in range(N):
        for m in range(n+1, N):
            dis = abs(island[n][0]-island[m][0])**2 + abs(island[n][1]-island[m][1])**2
            dis = dis*E
            G[n].append([m, dis])
            G[m].append([n, dis])

    PRIM()
    print('#{} {}'.format(tc, round(result)))

