# 1213_String-활용 풀이
# 2022-02-16

import sys
sys.stdin = open('test_input.txt', 'r', encoding='UTF-8')
T = 10

# 문자열 길이 구하는 함수
def length(s):
    c = 0
    for _ in s:
        c += 1
    return c

for tc in range(1, T+1):
    TN = int(input())  # 테스트 케이스의 번호
    p = input()        # 찾고자 하는 패턴
    t = input()        # 패턴이 담긴 text
    len_p = length(p)  # 패턴 길이
    len_t = length(t)  # text 길이
    cnt = 0            # 결과값

    # 문자열의 길이만큼 잘라서 통째로 비교
    # text 길이 - 패턴 길이 +1 회 수행
    for i in range(len_t - len_p+1):
        # 슬라이싱 한 패턴이 원하는 패턴이면 cnt + 1
        if t[i:i+len_p] == p:
            cnt += 1

    print('#{} {}'.format(TN, cnt))

