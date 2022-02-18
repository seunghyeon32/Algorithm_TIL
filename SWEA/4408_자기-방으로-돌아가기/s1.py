# 4408_자기-방으로-돌아가기 풀이
# 2022-02-18

import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):

    N = int(input())  # 자기 방으로 돌아가야 할 학생들의 수
    room = [0] * 200  # 0번인덱스 제외 방의 개수 200개
    result = 0        # 결과

    for _ in range(N):
        A, B = map(int, input().split())   # A: 현재방의 위치, B: 돌아갈 방의 위치

        # 홀수일때, 짝수로 변경
        A += 1 if A % 2 else 0
        B += 1 if B % 2 else 0

        # 방의 위치를 인덱스로 표현
        A = A // 2 - 1
        B = B // 2 - 1

        # 돌아갈 방의 인덱스가 더 크면, A <-> B로 계산
        if B < A:
            A, B = B, A

        # A에서 B까지 이동한 길에 +1을 해준다
        n = A
        while n <= B:
            room[n] += 1
            n += 1

    # 가장 많이 겹친 횟수 = 한번에 이동가능한 횟수
    for n in range(N, 0, -1):
        if n in room:
            result = n
            break

    print('#{} {}'.format(tc, result))



