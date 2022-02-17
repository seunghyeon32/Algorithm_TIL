# 6485_삼성시의-버스-노선 풀이
# 2022-02-17

import sys

sys.stdin = open('s_input.txt', 'r')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())    # 버스 노선 개수
    bus = list()        # 버스가 이동하는 정류장 범위
    c = list()          # 구하고자하는 정류장

    # 버스 정류장 범위 받아오기
    for n in range(1, N + 1):
        bus.append(list(map(int, input().split())))

    # 정류장 개수
    P = int(input())

    # 구하고자하는 정류장 번호
    for p in range(P):
        c.append(int(input()))

    # 정류장을 지나가는 버스 대수
    counts = [0] * P

    # 버스가 지나가는 범위 내에
    # 정류장이 있으면, 개수 + 1
    for i in range(N):
        for p in range(P):
            if bus[i][0] <= c[p] <= bus[i][1]:
                counts[p] += 1

    print('#{}'.format(tc), end='')
    for count in counts:
        print(' {}'.format(count), end='')
    print()
