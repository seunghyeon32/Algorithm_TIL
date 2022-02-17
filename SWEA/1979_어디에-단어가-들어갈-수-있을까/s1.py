# 1979_어디에-단어가-들어갈-수-있을까 풀이
# 2022-02-15

import sys

sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    # N: 배열의 크기 N*N
    # K: 단어의 길이
    # where: 2차원 배열 만들기
    # result: 결과값
    N, K = map(int, input().split())
    where = list()
    result = 0

    # 배열 만들기
    for _ in range(N):
        v = list(map(int, input().split()))
        where.append(v)

    # 배열 내부 살펴보자 !
    for i in range(N):
        cnt_r = 0           # 행에 1이 연속인지 확인
        cnt_c = 0           # 열에 1이 연속인지 확인

        for j in range(N):

            # 가로로 보기
            # 1이면 개수 +1
            # 0일때, 연속되는 개수가 3개면 result +1 & 개수 초기화
            # 0일때는 개수 초기화 !
            if where[i][j] == 1:
                cnt_r += 1
            else:
                if cnt_r == K:
                    result += 1
                cnt_r = 0

            # 세로로 보기
            if where[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    result += 1
                cnt_c = 0

        # 개수가 K개면 cnt + 1
        if cnt_r == K:
            result += 1

        if cnt_c == K:
            result += 1

    print('#{} {}'.format(tc, result))