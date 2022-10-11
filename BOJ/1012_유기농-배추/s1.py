# 1012 유기농 배추


def bfs(i, j, k):
    global check

    front = -1
    rear = 0
    queue = [(i, j)]

    while front < rear:
        front += 1
        si, sj = queue[front]

        # 4방향 탐색
        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ci, cj = si + di, sj + dj

            # 배열 범위 내에 있고, 배추가 심겨져있지만 확인한 적이 없다면 방문처리
            if 0 <= ci < H and 0 <= cj < W and arr[ci][cj] and not check[ci][cj]:
                queue.append((ci, cj))
                check[ci][cj] = k
                rear += 1


T = int(input())

for _ in range(T):
    W, H, k = map(int, input().split())
    arr = [[0] * W for _ in range(H)]
    check = [[0] * W for _ in range(H)]
    location = []
    position = 1

    # 배추 위치 구하기
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
        location.append((y, x))

    for h, w in location:
        # 아직 연결되지 않았지만, 배추가 있다면 bfs
        if not check[h][w] and arr[h][w]:
            bfs(h, w, position)
            position += 1

    print(position-1)