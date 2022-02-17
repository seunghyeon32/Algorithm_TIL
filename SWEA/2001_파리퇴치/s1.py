# 2001_파리퇴치 풀이
# 2022-02-15

import sys

sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):

    # N*N: 파리가 갇혀있는 공간 수, M*M: 파리채를 맞을 공간 수
    N, M = map(int, input().split())
    nums = list()
    sums = list()

    # 파리집 만들기
    for _ in range(N):
        v = list(map(int, input().split()))
        nums.append(v)

    # 파리잡기
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0    # 죽은 파리의 합 초기화

            # 죽은 파리의 합 구하기
            for p in range(M):
                for q in range(M):
                    s += nums[i+p][j+q]

            # 죽은 파리의 합들 모으기
            sums.append(s)

    # 최댓값 초기화
    max_dead = sums[0]

    # 최댓값 구하기
    for i in range((N-M+1)*(N-M+1)):
        if max_dead <= sums[i]:
            max_dead = sums[i]

    print('#{} {}'.format(tc, max_dead))