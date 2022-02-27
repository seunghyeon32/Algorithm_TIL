# 전기버스 풀이
# 2022-02-27

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # K: 한 번 충전으로 이동할 수 있는 최대 정류장 수
    # N: 0~N번 정류장
    # M: 충전기가 설치된 정류장 수
    # chargers: 충전기가 있는 정류장 위치
    # now: 현재 위치, cnt: 충전 횟수
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    now = 0
    cnt = 0

    while now < N:
        hi = 0  # 현재 상태 확인

        # 내 위치 + K부터 충전기가 있는지 확인
        for i in range(now+K, now, -1):
            # 충전기가 있다면, 내 위치를 이동하고, cnt + 1
            if i in charger:
                now = i
                cnt += 1
                hi = 1
                break

            # 도착했당 !
            if i >= N:
                hi = 2
                break

        # 이동할 수 있는거리에 충전기가 없다면, 0반환
        if hi == 0:
            cnt = 0
            break

        # 도착했당 !
        if hi == 2:
            break

    print('#{} {}'.format(tc, cnt))
