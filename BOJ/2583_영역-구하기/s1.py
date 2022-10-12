# 2583 영역 구하기


def bfs(i, j):
    global visit

    visit[i][j] = 1
    cnt = 1
    front = -1
    rear = 0
    queue = [(i, j)]

    while front < rear:
        front += 1
        si, sj = queue[front]

        for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
            ni, nj = si + di, sj + dj
            if 0 <= ni < H and 0 <= nj < W and not arr[ni][nj] and not visit[ni][nj]:
                rear += 1
                visit[ni][nj] = 1
                queue.append((ni, nj))
                cnt += 1

    return cnt


W, H, K = map(int, input().split())
arr = [[0] * W for _ in range(H)]
visit = [[0] * W for _ in range(H)]
c = 0
result = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1

for h in range(H):
    for w in range(W):
        if not arr[h][w] and not visit[h][w]:
            c += 1
            val = bfs(h, w)
            result.append(val)

result.sort()
print(c)
print(' '.join(str(x) for x in result))