# 1865_동철이의-일분배 풀이
# 2022-03-31
import sys
sys.stdin = open('input.txt', 'r')


def dfs(si, vj, p):
    global result

    if si == N:           # 마지막 행까지 다 돌았으면
        if result < p:    # 결과 비교 후, 바꿔줌
            result = p
        return

    if p < result:        # 가지치기
        return

    for j in range(N):
        if j not in vj and percents[si][j]:
            dfs(si+1, vj+[j], p*percents[si][j]/100)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percents = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    dfs(0, [], 1)
    print('#%d %.6f' % (tc, result*100))
