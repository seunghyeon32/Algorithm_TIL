# 4861_회문 풀이
# 2022-02-17

import sys

sys.stdin = open('sample_input.txt', 'r', encoding='UTF-8')
T = int(input())

for tc in range(1, T+1):
    # N: N*N 글자판, M: 회문의 길이
    # v: 글자판
    N, M = map(int, input().split())
    v = list()

    # 글자판 만들기
    for _ in range(N):
        v.append(input())

    for j in range(N):
        for i in range(N-M+1):
            compare_r = v[j][i:i+M]  # 글자판에서 회문을 확인할 행 문자열
            compare_c = ''           # 글자판에서 회문을 확인할 열 문자열
            result_r = 0             # 행이 회문인가 > 회문이면 0, 아니면 1
            result_c = 0             # 열이 회문인가 > 회문이면 0, 아니면 1

            # 회문을 확인할 열 만들기
            for p in range(M):
                compare_c += v[i+p][j]

            # compare_r, compare_c의 회문여부 판별
            for m in range(M//2):
                # 만일 회문이 아닐 경우, result_r = 1 or result_c = 1
                if compare_r[m] != compare_r[-m-1]:
                    result_r = 1
                if compare_c[m] != compare_c[-m-1]:
                    result_c = 1

            # 회문일 경우, 해당 회문 출력 후 끝 !!
            if result_r == 0:
                print('#{} {}'.format(tc, compare_r))
                break
            if result_c == 0:
                print('#{} {}'.format(tc, compare_c))
                break

        # 회문일 경우, 끝 !!
        if result_c == 0 or result_r == 0:
            break