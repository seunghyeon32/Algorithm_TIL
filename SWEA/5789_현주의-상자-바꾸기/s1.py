# 5789_현주의-상자-바꾸기
# 2022-02-10

import sys
#
# # input.txt 불러오기
# 테스트 케이스
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):

    # N: 상자의 개수, Q: 작업할 횟수
    # box: N개의 상자 만들기
    N, Q = map(int, input().split())
    box = [0] * N

    # 작업을 Q번 반복
    for q in range(Q):

        # L번 ~ R번 상자까지의 값을 q+1로 변경
        L, R = map(int, input().split())

        # 상자의 인덱스는 상자번호-1
        for idx in range(L-1, R):
            box[idx] = q+1

    print('#{}'.format(tc), end='')

    for i in range(N):
        if i == N-1:
            print(' {}'.format(box[i]))
        else:
            print(' {}'.format(box[i]), end='')

