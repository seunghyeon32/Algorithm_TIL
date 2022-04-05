# 5251_최소-이동-거리
# 2022-03-29

import sys

sys.stdin = open('sample_input.txt', 'r')


def dfs(v, distance, visited):
    global result

    if distance > result:            # 계산 중 저장된 최소값보다 거리가 크면 return(안하면, 시간초과)
        return

    if v == N:                       # N에 도착하면
        if result > distance:        # 거리가 최소값이면, 결과를 바꿔줌 !
            result = distance
        return

    # 갈 수 있는 경로 탐색
    for i in graph[v]:
        if not visited[i[0]]:        # 방문한 적 없는 노드일 때
            visited[i[0]] = True
            dfs(i[0], distance + i[1], visited)   # 더 깊이 들어가 !
            visited[i[0]] = False


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

    dfs(0, 0, visit)
    print('#{} {}'.format(tc, result))
