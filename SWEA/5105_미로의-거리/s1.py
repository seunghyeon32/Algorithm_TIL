# 5105_미로의-거리 풀이
# 2022-03-22
import sys
sys.stdin = open('sample_input.txt', 'r')


def bfs(v):
    global arr
    global counts

    queue = list()
    front = -1
    rear = 0
    queue.append(v)

    while front < rear:
        front += 1
        sy, sx = queue[front]

        # 델타탐색: 하 > 상 > 우 > 좌
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            cy = sy + dy
            cx = sx + dx

            # 길이 있을 때
            if 0 <= cy < N and 0 <= cx < N and arr[cy][cx] == 0 and not counts[cy][cx]:
                counts[cy][cx] = counts[sy][sx] + 1
                queue.append((cy, cx))
                rear += 1

            # 목적지를 찾았을 때
            if 0 <= cy < N and 0 <= cx < N and arr[cy][cx] == 3:
                print('#{} {}'.format(tc, counts[sy][sx]))
                return

    print('#{} {}'.format(tc, 0))


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]
    counts = [[0]*N for _ in range(N)]        # 이동 칸 수 누적합을 저장할 리스트

    for i in range(N):
        for j in range(N):
            # 출발점에서 출발 !
            if arr[i][j] == 2:
                counts[i][j] = 0
                bfs((i, j))
                break
