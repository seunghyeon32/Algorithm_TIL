# 1486_장훈이의-높은-선반 풀이
# 2022-03-21

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    result = sum(heights)

    # 만일 선반과 같은 키인 사람이 있다면, 0 출력
    if B in heights:
        print('#{} {}'.format(tc, 0))
    else:
        # 부분집합 구하기
        for i in range(1 << N):
            val = 0    # 부분집합의 값을 더해 저장할 변수
            for j in range(N):
                if i & (1 << j):
                    val += heights[j]

            # 키의 합이 선반보다 크거나 같고, result에 저장된 값보다 작을 때, 바꿔준다 !
            if val >= B and val-B < result:
                result = val-B

        print('#{} {}'.format(tc, result))