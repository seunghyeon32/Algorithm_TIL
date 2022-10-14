# 18352 특정 거리의 도시 찾기

from collections import deque


def bfs():
    global visited
    queue = deque([X])
    visited[X] = 1

    while queue:
        q = queue.popleft()

        for i in arr[q]:
            if not visited[i]:
                visited[i] = visited[q] + 1

                if visited[i] == K + 1:
                    result.append(i)
                    continue

                queue.append(i)


N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
result = []

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

bfs()

if result:
    result.sort()
    for r in result:
        print(r)
else:
    print(-1)


'''
4 4 2 1
1 2
1 3
2 3
2 4
'''