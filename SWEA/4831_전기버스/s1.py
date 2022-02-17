# 4831_전기버스
# 2022-02-10

import sys

# input.txt 불러오기
# 테스트 케이스
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    # v: K, N, M 받아올 변수
    # K: 한 번 충전으로 이동할 수 있는 최대 정류장 수
    # N: 0~N번 정류장
    # M: 충전기가 설치된 정류장 수
    # chargers: 충전기가 있는 정류장 위치
    # station: 정류장 (0-충전기 없음, 1-충전기 있음)
    # cnt: 최소 충전횟수
    # where: 충전소 위치를 찾기 위해 사용할 리스트
    v = list(map(int, input().split()))
    K, N, M = v[0], v[1], v[2]
    charges = list(map(int, input().split()))
    stations = [0] * (N+K)
    cnt = 0
    where = list()


    # 정류장에 충전기 여부 저장
    for charge in charges:
        stations[charge] = 1

    # 현재위치 초기화
    i = 0

    while i < N:
        # 현재 위치부터 이동가능한 위치까지의 충전소 정보 저장
        where = stations[i:i+K+1]

        # 이동할 칸 수 저장
        n = 0

        # 도착하면 끝 !
        if i + K >= N:
            break

        # 최소한의 충전을 요하므로 가장 먼 충전소 찾기
        for jump in range(K,-1, -1):

            # 충전소가 있을때, 현재 위치에서 충전소 위치로 이동하고 충전횟수 +1
            if where[jump] == 1:

                # 충전소 위치가 잘못되어 종점에 도착할 수 없는 경우, 반복문 종료 및 0반환
                # 현재 위치의 인덱스가 0이므로, 0에 충전소가 있으면 이동할 곳이 없음을 의미 !
                if jump == 0:
                    i = N
                    cnt = 0
                    break

                # 충전소 위치가 올바른 경우
                n = jump
                i = i + n
                cnt += 1
                break


    print('#{} {}'.format(tc, cnt))


