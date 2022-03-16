# 5099_피자-굽기 풀이
# 2022-03-15

import sys
sys.stdin = open('sample_input.txt', 'r')


def melting_num(n):   # 회전해야 하는 횟수
    cnt = 0
    while n > 0:
        n = n // 2
        cnt += 1
    return cnt


T = int(input())       # 테스트 케이스 개수
for tc in range(1, T+1):
    N, M = map(int, input().split())              # N: 화덕의 크기, M: 피자 개수
    cheeses = list(map(int, input().split()))     # cheeses: M개의 피자에 뿌려진 치즈의 양
    pizzas = [0] * N                              # 화덕에 있는 피자 번호

    # 각 피자마다 녹아야하는 횟수
    for i in range(M):
        cheeses[i] = melting_num(cheeses[i])

    # 화덕에 처음 든 피자 번호
    for j in range(N):
        pizzas[j] = j

    c = 0
    while pizzas[c%N] <= M+1 or cheeses[pizzas[c%N]] != 0:

        # 피자가 다 구워짐 >> 다음 피자 구워줘 !
        if pizzas[c%N] == M+1:
            c += 1
            continue

        cheeses[pizzas[c % N]] -= 1  # 치즈 한번 녹았다 = 한 바퀴 돌았다 !

        # 하나의 피자만 남았을 때, 그 피자 번호 반환해줘 !
        if cheeses.count(0) == M-1 and cheeses.count(1) == 1:
            print('#{} {}'.format(tc, cheeses.index(1)+1))
            break

        # 치즈가 다 녹았고, 더 구울 피자가 있다면 >> 다 녹은 피자는 빼고, 다음 피자 그 자리에 넣어줘 !
        # 치즈가 다 녹았는데, 더 구울 피자가 없다면 >> 다 녹은 피자 빼고, 더 넣을 피자가 없다고 표시해줘 (M+1) !
        if cheeses[pizzas[c%N]] == 0 and max(pizzas)+1 < M:
            pizzas[c%N] = max(pizzas)+1
        elif cheeses[pizzas[c%N]] == 0 and max(pizzas)+1 >= M:
            pizzas[c%N] = M + 1
        c += 1





