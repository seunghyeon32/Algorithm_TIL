# 1953_탈주범-검거 풀이
# 2022-03-16

import sys
sys.stdin = open('sample_input.txt', 'r')


# 델타탐색할 방향
def delta(num):
    if num == 1:
        return [(0, 1), (1, 0), (0, -1), (-1, 0)]
    elif num == 2:
        return [(1, 0), (-1, 0)]
    elif num == 3:
        return [(0, 1), (0, -1)]
    elif num == 4:
        return [(0, 1), (-1, 0)]
    elif num == 5:
        return [(1, 0), (0, 1)]
    elif num == 6:
        return [(0, -1), (1, 0)]
    elif num == 7:
        return [(0, -1), (-1, 0)]
    return []


def bfs(v):
    global underground
    global result
    global L

    front = -1
    rear = 0
    queue = [v]

    while front != rear:
        front += 1
        start = queue[front]

        si = start[0]
        sj = start[1]
        delta_v1 = delta(underground[si][sj])   # 현재 위치의 델타 값

        # 만일 시간 완료되면 끝 !
        if visit[si][sj] == L-1:
            return

        for di, dj in delta_v1:
            ci = si + di
            cj = sj + dj

            if 0 <= ci < N and 0 <= cj < M and visit[ci][cj] == 0 and underground[ci][cj] != 0:
                delta_v2 = delta(underground[ci][cj])   # 갈 수 있는 위치의 델타 값
                if delta_v2:
                    for dy, dx in delta_v2:
                        cy = ci + dy
                        cx = cj + dx
                        if 0 <= cy < N and 0 <= cx < M and si == cy and sj == cx:
                            result += 1
                            visit[ci][cj] = visit[si][sj] + 1
                            queue.append([ci, cj])
                            rear += 1


T = int(input())
for tc in range(1, T+1):
    # N: 세로크기, M: 가로크기, R: 맨홀세로위치, C: 맨홀가로위치, L: 소요된 시간
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    result = 0
    bfs([R, C])

    if result == 0:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, result))