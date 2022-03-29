# 1970_쉬운-거스름돈 풀이
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())//10*10
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    check = [0] * 8

    # 돈세기
    i = 0
    while i < 8:
        # 만일 거슬러줄 수 있다면,
        if N - money[i] >= 0:
            check[i] += 1   # 해당지폐로 거슬러 준다 !
            N -= money[i]
        # 거슬러 줄 수 없다면, 더 작은 잔돈을 찾는다 !
        else:
            i += 1

    print('#{}'.format(tc))
    print(*check)
