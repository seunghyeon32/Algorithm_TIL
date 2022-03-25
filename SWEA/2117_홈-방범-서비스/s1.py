# 2117_홈-방법-서비스 풀이
# 2022-03-22

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N: 도시의 크기, M: 하나의 집이 지불 할 수 있는 비용
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cost = [0] + [(n**2 + (n-1)**2) for n in range(1, N*2)]     # 운영비용
    home = list()  # 집이 있는 곳의 좌표
    ans = 0

    # 집의 좌표 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home += [(i, j)]

    # 완전탐색
    for n in range(N):
        for m in range(N):
            distance = [0] * (2*N)    # 인덱스만큼의 거리에 있는 집의 개수

            # 각 거리별로 존재하는 집의 개수 저장
            for di, dj in home:
                d = abs(n-di) + abs(m-dj) + 1
                distance[d] += 1

            for k in range(1, len(distance)):
                # 거리가 k인 마름모 내부의 집들까지 더하기
                distance[k] += distance[k-1]

                # 손해를 보지 않고, 가장많이 서비스를 제공할 수 있는 집 구하기
                if cost[k] <= distance[k] * M and distance[k] > ans:
                    ans = distance[k]

    print('#{} {}'.format(tc, ans))
