# 1953_탈주범-검거 풀이
# 2022-03-16

import sys
sys.stdin = open('sample_input.txt', 'r')


# 오른쪽 탐색
def right(i, j):
    global graph
    global underground
    if 0 <= i < N and 0 <= j + 1 < M:
        if underground[i][j + 1] in (1, 3, 6, 7):
            graph[i * M + j + 1].append(i*M+j+2)
            return


# 아래 탐색
def bottom(i, j):
    global graph
    global underground
    if 0 <= i + 1 < N and 0 <= j < M:
        if underground[i + 1][j] in (1, 2, 4, 7):
            graph[i * M + j + 1].append((i+1)*M+j+1)
            return


# 왼쪽 탐색
def left(i, j):
    global graph
    global underground
    if 0 <= i < N and 0 <= j-1 < M:
        if underground[i][j-1] in (1, 3, 4, 5):
            graph[i * M + j + 1].append(i*M+j)
            return


# 위쪽 탐색
def top(i, j):
    global graph
    global underground
    if 0 <= i-1 < N and 0 <= j < M:
        if underground[i-1][j] in (1, 2, 5, 6):
            graph[i * M + j + 1].append((i-1)*M + j + 1)
            return


# bfs
def bfs(v):
    queue = [[v]]      # queue 초기화
    cnt = 1            # 시간 카운팅
    result = 1         # 결과

    while queue:
        starts = queue.pop()          # 탐색할 레벨
        cnt += 1                      # 시간 + 1
        v = list()                    # 같은 레벨 받아올 리스트
        for start in starts:          # 한 레벨을 순회하기
            visit[start] = 1          # 방문 표시
            if not graph[start]:      # 연결된 곳이 없으면 패스
                continue

            for i in graph[start]:    # 연결된 곳 다 탐색
                if not visit[i]:      # 방문한 적이 없을 때
                    visit[i] = 1      # 방문 표시
                    result += 1       # 결과 + 1
                    v.append(i)       # 다음 레벨 값들 저장

        # L시간이 되면 끝 !
        if cnt == L:
            print('#{} {}'.format(tc, result))
            return
        queue.append(v)


T = int(input())
for tc in range(1, T+1):
    # N: 세로크기, M: 가로크기, R: 맨홀세로위치, C: 맨홀가로위치, L: 소요된 시간
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * (N*M+1)
    graph = [[] for _ in range(N*M+1)]

    # graph 만들기
    for i in range(N):
        for j in range(M):
            if underground[i][j] == 0:
                continue
            elif underground[i][j] == 1:
                right(i, j)
                bottom(i, j)
                left(i, j)
                top(i, j)
                continue
            elif underground[i][j] == 2:
                top(i, j)
                bottom(i, j)
                continue
            elif underground[i][j] == 3:
                right(i, j)
                left(i, j)
                continue
            elif underground[i][j] == 4:
                top(i, j)
                right(i, j)
                continue
            elif underground[i][j] == 5:
                bottom(i, j)
                right(i, j)
                continue
            elif underground[i][j] == 6:
                left(i, j)
                bottom(i, j)
            elif underground[i][j] == 7:
                top(i, j)
                left(i, j)

    bfs(R*M+C+1)
