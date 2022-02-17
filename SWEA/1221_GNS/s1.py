# 1221_GNS 풀이
# 2022-02-16

import sys
sys.stdin = open('GNS_test_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    # tn: 테스트번호, tn: 문자열길이
    # nums: 인덱스번호와 일치하는 영문자를 값으로 저장
    # counts: 해당 숫자가 나온 횟수 저장
    # in_nums: 문자열을 리스트로 받아옴
    tn, tl = map(str, input().split())
    tl = int(tl)
    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    counts = [0] * 10
    in_nums = list(map(str, input().split()))

    # in_nums에 해당하는 숫자의 횟수 카운팅
    for i in range(tl):
        for j in range(10):
            if in_nums[i] == nums[j]:
                counts[j] += 1

    # 문자열로 초기화
    in_nums = ''

    # in_nums 문자열에 해당 숫자가 나온 횟수만큼 영문 값 반환
    for n in range(10):
        in_nums += (nums[n] + ' ') * counts[n]

    print(tn)
    print(in_nums)

