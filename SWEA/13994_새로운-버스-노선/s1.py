# 13994_새로운-버스-노선 풀이
# 2022-SW-EA
import sys
sys.stdin = open('sample_in.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())      # 버스의 개수
    counts = [0] * 1001   # 버스가 몇 대 지나가는 지 확인

    for _ in range(N):
        # bus_type: 버스 종류
        # A: 시작 정류장, B: 도착 정류장
        bus_type, A, B = map(int, input().split())

        # 일반버스는 A, B까지 모두 지남
        if bus_type == 1:
            for n in range(A, B+1, 1):
                counts[n] += 1

        # 급행버스는 A가 짝수일때, 짝수만
        # A가 홀수일 때, 홀수만 지남
        elif bus_type == 2:
            for n in range(A, B, 2):
                counts[n] += 1
            counts[B] += 1

        # 광역급행버스는 A가 짝수일 때, 4의 배수만
        # 홀수일 때, 3의 배수이고 10의 배수가 아닌 정류장만
        elif bus_type == 3:
            if not A%2:
                if not A%4:
                    for n in range(A, B, 4):
                        counts[n] += 1
                    counts[B] += 1

                else:
                    counts[A] += 1
                    for n in range(A+2, B, 4):
                        counts[n] += 1
                    counts[B] += 1

            else:
                for n in range(A, B, 1):
                    if n == A or (not n%3) and (n%10):
                        counts[n] += 1
                counts[B] += 1

    result = max(counts)
    print('#{} {}'.format(tc, result))