# 1240_단순-2진-암호코드 풀이
# 2022-03-22

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lock = [list(map(int, input())) for _ in range(N)]   # 암호코드가 숨겨진 배열
    # 인덱스의 값: 해독할 수 / 값: 암호화된 배열
    nums = [
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 1]]

    # 암호문 찾기
    for n in range(N):
        if lock[n].count(1) > 0:
            val = lock[n]
            break

    # 암호문 찾기
    while val[-1] == 0:
        val.pop(-1)
    val = val[-56:]

    # 비밀번호 구하기
    secret = [0] * 8
    for i in range(0, 56, 7):
        num = val[i:i+7]
        for j in range(10):
            if num == nums[j]:
                secret[i//7] = j
                break

    # 검증하기
    check = 0
    for n in [0, 2, 4, 6]:
        check += secret[n]

    check *= 3

    for i in [1, 3, 5, 7]:
        check += secret[i]

    if not check%10:
        print('#{} {}'.format(tc, sum(secret)))
    else:
        print('#{} {}'.format(tc, 0))
