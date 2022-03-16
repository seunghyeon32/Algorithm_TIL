# 5102_노드의-거리 풀이
# 2022-03-15

import sys
sys.stdin = open('sample_input.txt', 'r')


# a에서 b까지
def bfs(a, b):
    global visit

    visit[a] = True   # 시작점 방문 처리
    queue = [[a]]     # 횟수가 필요한 문제이므로 리스트안에 리스트를 만들어줌
    cnt = 0           # 횟수 카운팅 변수

    # queue가 빌 때까지
    while queue:
        starts = queue.pop(0)
        cnt += 1
        v = list()    # 같은 레벨의 값들을 저장할 리스트

        # 한 레벨을 묶어서 보기 때문에 반복문을 돌림
        for start in starts:
            for i in graph[start]:
                if i == b:   # 도착지를 찾으면, 횟수 출력 후 종료
                    print('#{} {}'.format(tc, cnt))
                    return

                if not visit[i]:       # 방문기록이 없으면
                    visit[i] = True    # 방문 표시
                    v.append(i)        # 경로 추가

        if not v:  # 도착지에 도달하지 못하면, 0 출력 후 종료
            print('#{} {}'.format(tc, 0))
            return

        queue.append(v)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # V: 노드 개수, E: 간선의 개수
    graph = [[] for _ in range(V+1)]  # graph: 연결상태를 저장할 변수
    visit = [False] * (V+1)           # 방문기록을 저장할 변수

    # graph 만들기
    # 방향성이 없으므로, 양방향으로 만들었음 !
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    # S: 시작노드번호, G: 도착노드번호
    S, G = map(int, input().split())
    bfs(S, G)
