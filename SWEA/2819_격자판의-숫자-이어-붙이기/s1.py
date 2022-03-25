# 2819_격자판의-숫자-이어-붙이기 풀이
# 2022-03-25

import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(n, num, i, j):
    global sset
    if n == 7:
        sset.add(num)
        return

    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ci = i + di
        cj = j + dj
        if 0 <= ci < 4 and 0 <= cj < 4:
            dfs(n+1, num*10+arr[ci][cj], ci, cj)


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    sset = set()

    for y in range(4):
        for x in range(4):
            dfs(0, 0, y, x)

    print('#{} {}'.format(tc, len(sset)))