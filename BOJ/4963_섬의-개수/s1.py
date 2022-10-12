# 4963 섬의 개수


def bfs(i, j):
    global visit

    front = -1
    rear = 0
    queue = [(i, j)]

    while front < rear:
        front += 1
        si, sj = queue[front]

        for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, -1), (-1, 1):
            ni, nj = si + di, sj + dj
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] and not visit[ni][nj]:
                rear += 1
                queue.append((ni, nj))
                visit[ni][nj] = 1


while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0: break

    arr = [list(map(int, input().split())) for _ in range(H)]
    visit = [[0] * W for _ in range(H)]
    result = 0

    for h in range(H):
        for w in range(W):
            if not visit[h][w] and arr[h][w]:
                result += 1
                bfs(h, w)

    print(result)