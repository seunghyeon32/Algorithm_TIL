# 4615_재미있는-오셀로-게임 풀이
# 2022-03-25
import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N // 2 - 1][N // 2 - 1], arr[N // 2][N // 2] = 2, 2
    arr[N // 2 - 1][N // 2], arr[N // 2][N // 2 - 1] = 1, 1
    white, black = 2, 1
    cnt = 4

    for _ in range(M):
        i, j, color = map(int, input().split())

        # 인덱스 맞추기
        i -= 1
        j -= 1

        # 8방향 탐색
        for di, dj in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
            k = 1

            while True:
                ci = i + k * di
                cj = j + k * dj

                # 인덱스 범위 내에 존재할 경우
                if 0 < ci < N and 0 <= cj < N:
                    if arr[ci][cj] == 0:          # 0을 만나면 넣을 수 없음
                        break
    
                    if arr[ci][cj] != color:      # 다른 색이 나오면 continue
                        k += 1
                        continue

                    if k == 1 and arr[ci][cj] == color:   # 내가 넣으려는 곳 바로 옆에 같은 색이 있으면, 넣을 수 없음
                        break

                    if k > 1 and arr[ci][cj] == color:    # 같은 색 돌과 나 사이에 다른 색 공들이 있으면, 바꾸고 넣어줌
                        di = -di
                        dj = -dj

                        for p in range(1, k + 1):
                            arr[ci + p * di][cj + p * dj] = color
                        break

                    k += 1

                else:
                    break
    
    # 백돌과 흑돌의 개수 구하기
    nw = 0
    nb = 0
    for i in range(N):
        nw += arr[i].count(2)
        nb += arr[i].count(1)

    print('#{} {} {}'.format(tc, nb, nw))
