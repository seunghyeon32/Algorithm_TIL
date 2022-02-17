# 4835_구간합
# 2022-02-10

import sys

# input.txt 불러오기
# 테스트 케이스
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    # N: 숫자의 개수, M: 구간의 개수
    # v: 숫자들을 저장할 리스트
    # sums: 각 구간의 숫자들의 합을 저장할 리스트
    # result: 결과를 저장할 변수
    N, M = map(int, input().split())
    v = list(map(int, input().split()))
    sums = [0]*(N-M+1)
    result = 0

    # 연속된 M개의 숫자들의 합을 sums 리스트에 저장
    # 초기시작은 M-1번째 인덱스에서 시작해 인덱스 에러 방지
    for i in range(M-1, N):

        # 구간의 합을 val에 저장
        val = 0
        for n in range(M):
            val += v[i-n]

        # 구간합 val을 sums 리스트에 저장
        sums[i-M] = val

    # 최대, 최소 합을 초기화
    max_sum = sums[0]
    min_sum = sums[0]

    # 최대합, 최소합 구하기
    for s in sums:
        if s >= max_sum:
            max_sum = s

        if s <= min_sum:
            min_sum = s

    # 최대합과 최소합의 차
    result = max_sum - min_sum

    print('#{} {}'.format(tc, result))
