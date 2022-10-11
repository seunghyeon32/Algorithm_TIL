# 1389 케빈 베이컨의 6단계 법칙

N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
connect = [[0] * N for _ in range(N)]
kevin = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    connect[a-1][b-1] = 1
    connect[b-1][a-1] = 1

def dfs(v, start, dep):
    global graph

    # 종료조건: 이미 더 작은 깊이가 이루어진 경우
    if 0 < connect[start][v] < dep:
        return

    # 연결된 모든 노드 탐색
    for i in range(N):
        # 시작노드와 동일하거나 자기 자신일 경우, 깊이탐색하지 않음
        if i == v or i == start: continue

        # 연결된 노드의 경우
        if graph[v][i]:
            # 시작점과 연결되지 않은 경우
            if not connect[start][i]:
                connect[start][i] = dep + 1

            # 더 얕은 깊이를 찾은 경우
            elif connect[start][i] > dep+1:
                connect[start][i] = dep + 1

            dfs(i, start, dep+1)


for n in range(N):
    dfs(n, n, 0)
    kevin[n] = sum(connect[n])

min_num = min(kevin)
result = kevin.index(min_num) + 1

print(result)

