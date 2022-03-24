# 1242_암호코드-스캔 풀이
# 2022-03-24
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                  '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                  'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    nums = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
            [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
    result = 0
    check = list()
    codes = list()

    # 중복 제거 및 2진수 변환
    for n in range(N):
        if arr[n] == '0'*M:
            continue
        else:
            val = ''
            for m in range(M):
                val += hex_to_bin[arr[n][m]]

            if val not in codes:
                codes.append(val)
            continue

    for code in codes:
        secret_num = [10] * 8    # 해독된 암호 저장할 리스트
        sn = 7                   # 뒤에서 부터 찾음
        start = 0                # 0: 찾는 중, 1: 해독 중

        for i in range(len(code)-1, -1, -1):
            # 신경 안써도 되는 구문
            if start == 0 and code[i] == '0':
                continue

            # 암호를 발견했다 !!
            if start == 0 and code[i] == '1':
                start = 1
                rate = [0]*4
                idx_r = 3

            # 암호 해독중
            if start == 1:
                if (idx_r%2 and code[i] == '1') or (not idx_r%2 and code[i] == '0'):
                    rate[idx_r] += 1
                else:
                    idx_r -= 1
                    rate[idx_r] += 1

                # idx_r = 0 이고, rate의 합이 7의 배수면,
                if not idx_r and not sum(rate)%7:
                    start = 0              # 숫자 찾았다 !
                    k = sum(rate) // 7     # 비율이 몇배인지
                    alt = rate[:]
                    # 합을 7로 만들기
                    if k != 1:
                        for j in range(4):
                            rate[j] //= k

                    # 비율이 이상하다 = 암호를 끝까지 해독하지 않았다
                    # 이어서 해줘 !
                    if sum(rate) != 7:
                        rate = alt[:]
                        start = 1
                        continue

                    # 해독할 비율은 nums에서 찾는다 !
                    secret_num[sn] = nums.index(rate)
                    sn -= 1

                    # 8자리 숫자를 다 찾았을 때,
                    if sn == -1:
                        sn = 7
                        # 확인한 적 없는 숫자면
                        if secret_num not in check:

                            # 올바른 암호인지 확인
                            v = 0
                            for h in range(8):
                                if h % 2:
                                    v += secret_num[h]
                                else:
                                    v += secret_num[h]*3

                            if not v % 10:
                                check.append(secret_num)
                                result += sum(secret_num)

                        secret_num = [10] * 8

    print('#{} {}'.format(tc, result))