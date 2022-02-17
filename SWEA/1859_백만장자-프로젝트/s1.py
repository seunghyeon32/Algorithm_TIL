# 1859_백만장자-프로젝트 풀이
# 2022-02-17
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = int(input())   # N: 각 날의 매매가 수
    prices = list(map(int, input().split())) # 매매가 리스트 저장
    result = 0         # 결과 변수
    n = 0              # while문 실행 변수

    while n < N:
        # 최댓값 찾기 (값, 인덱스)
        max_p = prices[n]
        max_i = n

        # 최댓값, 최댓값의 인덱스 구하기
        for i in range(n, N):
            if max_p < prices[i]:
                max_p = prices[i]
                max_i = i

        # 시작값부터 최댓값이 인덱스까지
        # 최댓값 - 현재위치의 값을 더해줌
        for j in range(n, max_i):
            result += (prices[max_i] - prices[j])

        # max인덱스의 다음 인덱스로 넘어감
        n += (max_i-n)+1

    print('#{} {}'.format(tc, result))
