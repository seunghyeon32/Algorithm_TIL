# 5203_베이비진-게임 풀이
# 2022-03-29
import sys
sys.stdin = open('sample_input.txt', 'r')


# run과 triple을 확인할 함수
def check(lst):
    for n in range(10):
        # run인 경우
        if n < 8 and 0 not in lst[n:n+3]:
            return 1
        # triple인 경우
        if lst[n] >= 3:
            return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    play1 = 0
    play2 = 0

    for i in range(0, 12, 2):
        player1[card[i]] += 1        # 짝수번 인덱스 = player1
        player2[card[i+1]] += 1      # 홀수번 인덱스 = player2

        # run과 triple확인 후, 하나라도 먼저 나오면 이김
        play1 = check(player1)
        if play1 == 1:
            break
        play2 = check(player2)
        if play2 == 1:
            break

    # 승부 결과 출력
    if play1 == play2:
        print('#{} {}'.format(tc, 0))
    elif play1 > play2:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 2))
