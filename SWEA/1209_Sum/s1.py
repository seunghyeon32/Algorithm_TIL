# 1209_Sum 풀이
# 2022-02-15

import sys

sys.stdin = open('input.txt', 'r')
T = 10

for tc in range(1, T+1):
    TN = int(input())    # 테스트 케이스 번호
    nums = list()        # 2차원 숫자 배열 저장
    sums = list()        # 각 행의 합, 각 열의 합, 대각선의 합 저장

    # 2차원 배열 만들기
    for _ in range(100):
        v = list(map(int, input().split()))
        nums.append(v)

    # 각 행의 합, 각 열의 합 구하기
    for i in range(100):
        sr = 0
        sc = 0
        for j in range(100):
            sr += nums[i][j]
            sc += nums[j][i]

        sums.append(sr)
        sums.append(sc)

    # 대각선의 합 구하기
    di = [1, 1]    # 오른쪽 아래, 왼쪽 아래
    dj = [1, -1]   # 오른쪽 아래, 왼쪽 아래
    cnt = 0        # 대각선 2개

    while cnt < 2:
        s = 0    # 대각선의 합 초기화

        # 오른쪽 아래로 진행 시, (0,0)에서 시작
        if cnt == 0:
            ci = 0
            cj = 0

        # 왼쪽 아래로 진행 시, (0,99)에서 시작
        elif cnt == 1:
            ci = 0
            cj = 99

        # 대각선의 합 구하기
        for _ in range(100):
            s += int(nums[ci][cj])
            ci += di[cnt]
            cj += dj[cnt]

        # 구한 대각선의 합 list에 추가
        sums.append(s)
        cnt += 1

    # 가장 큰 합 초기화
    max_num = sums[0]

    # 가장 큰 합 찾기
    for find_s in sums:
        if max_num <= int(find_s):
            max_num = int(find_s)

    print('#{} {}'.format(TN, max_num))