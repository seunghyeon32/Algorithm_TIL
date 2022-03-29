# 5189_전자카트
# 2022-03-29

import sys
sys.stdin = open('sample_input.txt', 'r')


def permutation(n, picked, topick):
    global result, arr
    if topick == 0:                 # 순열을 다 구했을 경우
        picked += [0]       # 사무실로 돌아와야 하기 때문에 0추가

        # 배터리 소비량 구하기
        v = 0
        for j in range(n):
            v += arr[picked[j]][picked[j+1]]

        # 최소 배터리 소비량 구하기
        if v < result:
            result = v

        return

    else:
        for i in range(1, n):
            if i not in picked:
                permutation(n, picked+[i], topick-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 100*N*N                 # 결과를 저장할 변수
    permutation(N, [0], N-1)         # 순열 구하기: 사무실에서 출발하기 때문에 초기값 = [0]
    print('#{} {}'.format(tc, result))