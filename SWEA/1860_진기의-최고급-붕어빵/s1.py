# 1860_진기의-최고급-붕어빵 풀이
# 2022-03-22
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort(reverse=True)
    cnt = 0       # 붕어빵 개수
    a = 0         # 붕어빵 만드는 중
    time = 0      # 영업시간
    p = 0         # impossible 표시

    while arrive:
        # 오픈시간에 도착하면 붕어빵 없어 !
        if arrive[-1] == 0:
            p = 1
            print('#{} Impossible'.format(tc))
            break

        a += 1
        time += 1
        # 붕어빵 만들어지면 K개 추가 !
        if a == M:
            cnt += K
            a = 0

        # 손님이 남았고, 손님이 지금 왔다면
        while arrive and time == arrive[-1]:
            # 붕어빵이 있다면, 손님에게 하나 주고 보냄
            if cnt:
                arrive.pop()
                cnt -= 1
            # 없다면, 붕어빵 없어요 !
            else:
                p = 1
                print('#{} Impossible'.format(tc))
                break

        if p == 1:
            break

    if p == 0:
        print('#{} Possible'.format(tc))