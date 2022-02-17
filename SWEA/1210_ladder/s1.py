# 1210_ladder 풀이
# 2022-02-15

import sys

# input 파일 열기
# 테스트 케이스 10개
sys.stdin = open('input.txt', 'r')
T = 10

for tc in range(1, 11):
    # 테스트 번호 받기
    TN = int(input())

    # 사다리를 만들 list
    ladder = list()

    # 사다리 만들기
    for _ in range(100):
        r = list(map(int, input().split()))
        ladder.append(r)

    # goal 찾기
    for j in range(100):
        if ladder[99][j] == 2:
            cj = j

    # 밑에서 위로 올라올거야 !
    ci = 99
    di = [0, 0, -1]   # 좌 우 상 (행)
    dj = [-1, 1, 0]   # 좌 우 상 (열)
    direction = 2     # 방향 설정

    # 행번호가 0번이면 끝 !
    while ci > 0:
        ci += di[direction]   # 현재위치 (행)
        cj += dj[direction]   # 현재위치 (열)

        # 오른쪽 왼쪽 살펴보기
        for d in range(2):
            li = ci + di[d]   # 오(왼)으로 갔을 때의 행
            lj = cj + dj[d]   # 오(왼)으로 갔을 때의 열

            # Overflow 방지
            if 0 <= li < 100 and 0 <= lj < 100:

                # 위로 가는 중일 때, 좌우를 살핀다.
                # 왼쪽이나 오른쪽에 길이 있으면 방향을 튼다.
                if ladder[li][lj] == 1 and direction == 2:
                    direction = d
                    break

                # 좌 또는 우로 진행하다가, 벽을 만나면 위로 간다.
                if ladder[li][lj] == 0 and direction == d:
                    direction = 2
                    break

            # 가상 이동 시, 행(열)이 인덱스 범위를 넘었을 경우 벽을 만난 것과 같다.
            # 위로 이동
            elif li < 0 or li >= 100 or lj < 0 or lj >= 100:
                direction = 2
                continue

    print('#{} {}'.format(TN, cj))

