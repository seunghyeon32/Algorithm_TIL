# 부분집합의-합
# 2022-02-12

import sys

# input.txt 불러오기
# 테스트 케이스
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):

    # N: 부분집합 원소의 개수, K: 부분집합 원소의 합
    # A: 1~12까지의 숫자를 원소로 하는 집합
    # parts:
    # result: 결과를 저장할 변수
    N, K = map(int, input().split())
    A = [n for n in range(1, 13)]
    parts = list()
    result = 0

    # 부분집합 구하기
    for i in range(1 << 12):
        cnt = 0                    # 원소의 수 초기화
        part = list()              # 부분집합

        for j in range(12):
            if i & (1 << j):
                cnt += 1           # 원소 수 세기
                part.append(A[j])  # 부분집합 만들기

        if cnt == N:               # 원소의 수가 N인 부분집합이면 추가
            parts.append(part)
            part = []
            cnt = 0

    # 부분집합들의 합 구하기
    for p in parts:
        val = 0

        # 부분집합 하나의 합 구하기
        for i in p:
            val += i

        # 부분집합의 합이 K이면, 하나 찾았당 !
        if val == K:
            result += 1
            val = 0

    print('#{} {}'.format(tc, result))
