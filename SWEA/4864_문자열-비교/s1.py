# 4864_문자열-비교 풀이
# 2022-02-17
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

def length(s):
    cnt = 0

    for _ in s:
        cnt += 1

    return cnt

for tc in range(1, T+1):
    str1 = input()          # pattern
    str2 = input()          # 전체 str
    N = length(str1)        # 패턴의 길이
    M = length(str2)        # 전체 길이
    result = 0              # 일치하는 문자개수

    for i in range(M-N+1):
        for j in range(N):
            # 만일 str1과 str2가 다르면, result 초기화 후
            # 다른 문자열 비교
            if str1[j] != str2[i+j]:
                result = 0
                break
            # str1과 str2의 문자가 같으면 개수 더하기
            else:
                result += 1

        # 일치하는 문자열의 개수 == 패턴의 길이면, 찾았다 !
        if result == N:
            print('#{} {}'.format(tc, 1))
            break

    # 그렇지 않으면, 못찾았다 !
    if result != N:
        print('#{} {}'.format(tc, 0))





    # counts = [0] * N        # counts == N 일때, 찾았다 !
    # m = 0                   # str2의 인덱스
    # current = 0             # 현재 위치
    # find = 0                # 1: 찾았다 0: 없다

    # while m < M:
    #     if m+N-1 >= M:
    #         break
    #     # 만약, 끝 값이 같다면 끝 값을 기준으로 고정
    #     if str1[-1] == str2[m+N-1]:
    #         counts[-1] += 1
    #
    #         # str1의 (-2)~0인덱스의 값들이 일치하는지 확인
    #         for n in range(-2, -N-1, -1):
    #             # 만일, 같으면 찾았다
    #             if str1[n] == str2[m+n]:
    #                 counts[n] += 1
    #
    #             # 다르면 counts에서 1이 제일 처음 나오는 위치로 돌아가야함.
    #             else:
    #                 fix = 0
    #
    #                 for i in range(N-1, -1, -1):
    #                     if counts[i] == 1 and fix == 0:
    #                         m = m + N - i
    #                         fix = 1
    #                     else:
    #                         counts[i] = 0
    #
    #     else:
    #         for n in range(-2, -N-1, -1):
    #             if str1[n] == str2[m + N]:
    #                 m = m - n
    #                 break
    #         m = m + N


    # print('#{} {}'.format(tc, find))
