# 5251_최소-이동-거리
# 2022-04-05

import sys
sys.stdin = open('sample_input.txt', 'r')


def Dijkstra(G, r):
    D = [999] * (N+1)  # 모든 정점들의 가중치를 저장할 리스트
    P = [None] * (N+1)  # 이전 경로를 저장할 리스트
    visited = [False] * (N+1)  # 그래프의 각 정점에 대해 방문여부를 저장
    D[r] = 0  # 출발지 r에 대한 가중치 값

    for _ in range(N):
        minIndex = -1
        mini = 999

        for i in range(N):  # 방문하는 정점 중 최소 가중치 정점을 찾는다.
            if not visited[i] and D[i] < mini:
                mini = D[i]
                minIndex = i
        visited[minIndex] = True  # 최소 가중치 정점 방문 처리

        for v, val in G[minIndex]:  # 선택 정점에 인접한 정점에 대해 반복
            # 방문하는 정점 중 선택하는 정점의 가중치 + 간선의 가중치 < v의 가중치면,
            # 선택한 정점을 거쳐 정점 v에 이르는 경로의 가중치 합 < 지금까지 찾은 출발점에서 정점 v까지 최단 경로 가중치 합
            # 더 짧은 경로로 갱신 (추후, 최단 경로를 추출할 때 사용하기 위해 이전 경로를 갱신)
            if not visited[v] and D[minIndex] + val < D[v]:
                D[v] = D[minIndex] + val
                P[v] = minIndex
    return D[-1]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N)]
    visit = [0] * (N + 1)
    result = 100000

    # 그래프 만들기
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    print('#{} {}'.format(tc, Dijkstra(graph, 0)))