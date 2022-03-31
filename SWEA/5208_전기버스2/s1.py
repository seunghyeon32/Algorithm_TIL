# 5208_전기버스2 풀이
# 2022-03-31

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    battery = list(map(int, input().split()))
    N = battery[0]
    battery = battery[1:]
    cnt = 0
    si = 0
    sb = battery[0]
    while True:
        md = 0
        mi = 0

        # 배터리로 이동할 수 있는 거리 중 가장 멀리 이동할 수 있는 배터리를 가진 정류장 찾기
        for i in range(si+1, si+sb+1):
            if i + battery[i] >= md:
                mi = i
                md = i + battery[i]

        si = mi
        sb = battery[si]
        cnt += 1

        # 현재 배터리로 종점까지 갈 수 있을 때, break 충전 완료 !
        if si + sb >= N-1:
            break

    print('#{} {}'.format(tc, cnt))