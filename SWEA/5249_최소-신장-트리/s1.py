# 5249_최소-신장-트리 풀이
# 2022-04-09

import sys
sys.stdin = open('sample_input.txt', 'r')


def MST_PRIM(s):
    global G, visit, distances, cnt, result

    cnt += 1
    if cnt == (V+1):  # 모든 노드 방문시, 끝 !
        return

    visit[s] = True   # 노드 방문처리
    min_idx = -1      # 최소 인덱스 초기값
    min_val = 99      # 최소 이동거리 초기값

    # 거리 정보를 distances에 저장
    for idx, dis in G[s]:
        if not visit[idx] and dis < distances[idx]:
            distances[idx] = dis

    # 방문안한 노드 중 최소 이동거리 찾기
    for n in range(V+1):
        if not visit[n] and distances[n] < min_val:
            min_idx = n
            min_val = distances[n]

    result += min_val   # 간선의 가중치 더하기
    MST_PRIM(min_idx)   # 가장 적은 가중치로 갈 수 있는 인덱스에서 더 찾아보기 !


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 0~V번까지의 노드 존재, E: 간선의 개수
    G = [[] for _ in range(V+1)]      # 그래프 정보
    visit = [False] * (V + 1)         # 방문 여부 초기화
    distances = [99] * (V + 1)        # 가중치를 무한대로 초기화
    cnt = 0                           # 노드 방문개수 체크
    result = 0                        # 가중치의 합

    # 그래프 만들기
    for e in range(E):
        n1, n2, w = map(int, input().split())
        G[n1].append([n2, w])
        G[n2].append([n1, w])

    distances[0] = 0  # 0번 노드에서 출발(거리=0으로 초기화)
    MST_PRIM(0)

    print('#{} {}'.format(tc, result))

