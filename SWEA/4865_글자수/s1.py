# 4865_글자수 풀이
# 2022-02-17
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

# len 함수: 문자열 길이 구하기
def leng(s):
    cnt = 0
    for _ in s:
        cnt += 1
    return cnt

for tc in range(1, T+1):
    # str1: 찾을 글자
    # str2: 글자가 포함된 문자열
    # N: str1 글자수
    # M: str2 글자수
    # counts: 각 문자의 개수를 담을 변수
    str1 = input()
    str2 = input()
    N = leng(str1)
    M = leng(str2)
    counts = [0] * N

    # 문자개수 구하기
    for n in range(N):
        for m in range(M):
            if str1[n] == str2[m]:
                counts[n] += 1

    # 해당 문자가 가장 많이 나온 횟수
    ma_c = counts[0]

    for c in counts:
        if max_c < c:
            max_c = c

    print('#{} {}'.format(tc, max_c))
