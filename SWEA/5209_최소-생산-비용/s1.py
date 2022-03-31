# 5209_최소-생산-비용 풀이
# 2022-03-31
import sys
sys.stdin = open('sample_input.txt', 'r')


def pick(n, picked, s, topick):
    global costs, result

    if s > result:          # 가지치기(Prunning)
        return

    if topick == 0:         # 순열을 다 찾은 경우
        if s < result:      # 최소 합을 찾는다 !
            result = s
        return

    for i in range(n):
        if i not in picked:  # 중복제거
            pick(n, picked + [i], s+costs[n-topick][i],topick-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int,input().split())) for _ in range(N)]
    result = 99*N
    pick(N, [], 0, N)
    print('#{} {}'.format(tc, result))