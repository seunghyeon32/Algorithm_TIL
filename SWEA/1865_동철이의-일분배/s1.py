# 1865_동철이의-일분배 풀이
# 2022-03-31
import sys
sys.stdin = open('input.txt', 'r')


def pick(n, picked, p, topick):
    global result

    if topick == 0:        # 순열 완성되면
        if p > result:     # p가 result보다 크다면 result = p
            result = p
        return

    # 가지치기
    if p < result:
        return

    for i in range(n):
        if i not in picked and percents[n-topick][i]:
            pick(n, picked+[i], p*percents[n-topick][i]/100, topick-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percents = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    pick(N, [], 1, N)
    print('#%d %.6f' % (tc, result*100))
