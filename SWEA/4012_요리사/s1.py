# 4012_요리사 풀이
# 2022-03-14

import sys
sys.stdin = open('sample_input.txt', 'r')


def part(lst, l):
    ps = list()

    for i in range(1 << N):
        cnt = 0
        p = list()

        for j in range(N):
            if i & (1 << j):
                cnt += 1
                p.append(lst[j])

        if cnt == N//2:
            ps.append(p)

    return ps


T = int(input())
for tc in range(1, T+1):
    N = int(input())                        # 식재료의 개수
    tastes = [list(map(int, input().split())) for _ in range(N)]  # 시너지 값 받아오기
    nums = list(range(N))                   # 0~(N-1)번호의 식재료
    parts = part(nums, N//2)  # N//2개의 원소를 갖는 부분집합
    result = 40000                          # 결과 초기화

    for i in range(N):                      # 대각선으로 접어서 다 더해버린다 !
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