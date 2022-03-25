# 2105_디저트-카페 풀이
# 2022-03-25
import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(n, ci, cj, v, cnt):
    global ans, i, j
    di = (1, 1, -1, -1, 0)
    dj = (-1, 1, 1, -1, 0)

    if n > 3:
        return
    if ci == i and cj == j and n == 3 and cnt > ans:
        ans = cnt
        return

    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            dfs(k, ni, nj, v+[arr[ni][nj]], cnt+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    for i in range(N):
        for j in range(N):
            dfs(0, i, j, [], 0)

    print('#{} {}'.format(tc, ans))