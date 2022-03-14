# 4012_요리사 풀이
# 2022-03-14

import sys
from itertools import combinations

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 식재료의 개수
    tastes = [list(map(int, input().split())) for _ in range(N)]
    nums = list(range(N))
    parts = list(combinations(nums, N//2))
    result = 40000

    for i in range(N):
        for j in range(i+1, N):
            tastes[i][j] += tastes[j][i]
            tastes[j][i] = 0

    for n in range(len(parts)//2):
        val = 0
        val2 = 0
        for p in range(N//2-1):
            for q in range(p+1, N//2):
                val += tastes[parts[n][p]][parts[n][q]]
                val2 += tastes[parts[-n-1][p]][parts[-n-1][q]]

        if abs(val-val2) < result:
            result = abs(val-val2)

    print('#{} {}'.format(tc, result))