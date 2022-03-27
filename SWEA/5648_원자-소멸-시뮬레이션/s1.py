# 5648_원자-소멸-시뮬레이션 풀이
# 2022-03-26

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 원자의 개수
    atoms = [list(map(int, input().split())) for _ in range(N)]   # 0, 1: 원자의 좌표, 2: 이동 방향, 3: 보유에너지
    bombs = [[] for _ in range(N)]    # 각각의 인덱스에 해당하는 원자가 만날 수 있는 원자들
    dis = set()          # 거리를 저장할 변수
    check = [0] * N      # 방문 표시
    result = 0

    # 0.5초를 1초로 만들어 주기 위해 모두 2배씩
    for p in range(N):
        atoms[p][0] *= 2
        atoms[p][1] *= 2

    # 원자가 만날 수 있는 원자들 구하기
    for i in range(N):
        for j in range(i+1, N):
            # x값이 같을 때
            if atoms[i][0] == atoms[j][0]:
                # j 기준: y가 큼 = 1, y가 작음 = 0
                if atoms[i][1] > atoms[j][1] and atoms[i][2] == 1 and atoms[j][2] == 0 or \
                        atoms[i][1] < atoms[j][1] and atoms[i][2] == 0 and atoms[j][2] == 1:
                    d = abs(atoms[i][1] - atoms[j][1]) // 2
                    dis.add(d)
                    if (d, j) not in bombs[i]:
                        bombs[i].append((d, j))
                    if (d, i) not in bombs[j]:
                        bombs[j].append((d, i))

            # y값이 같을 때
            if atoms[i][1] == atoms[j][1]:
                # j 기준: x가 큼 = 2, x가 작음 = 3
                if atoms[i][0] > atoms[j][0] and atoms[i][2] == 2 and atoms[j][2] == 3 or \
                        atoms[i][0] < atoms[j][0] and atoms[i][2] == 3 and atoms[j][2] == 2:
                    d = abs(atoms[i][0] - atoms[j][0]) // 2
                    dis.add(d)
                    if (d, j) not in bombs[i]:
                        bombs[i].append((d, j))
                    if (d, i) not in bombs[j]:
                        bombs[j].append((d, i))

            # 방향이 2일때, x좌표는 크고, 이동거리는 같아야 함.
            if atoms[i][0] > atoms[j][0] and atoms[i][2] == 2 and abs(atoms[i][0] - atoms[j][0]) == abs(
                    atoms[i][1] - atoms[j][1]):
                # j 기준: y가 크면 : 1, y가 작으면 : 0
                if atoms[i][1] > atoms[j][1] and atoms[j][2] == 0 or \
                        atoms[i][1] < atoms[j][1] and atoms[j][2] == 1:
                    d = abs(atoms[i][0] - atoms[j][0])
                    dis.add(d)
                    if (d, j) not in bombs[i]:
                        bombs[i].append((d, j))
                    if (d, i) not in bombs[j]:
                        bombs[j].append((d, i))

            # 방향이 3일때, x좌표는 작고, 이동거리는 같아야 함.
            if atoms[i][0] < atoms[j][0] and atoms[i][2] == 3 and abs(atoms[i][0] - atoms[j][0]) == abs(
                    atoms[i][1] - atoms[j][1]):
                # j 기준: y가 크면 : 1, y가 작으면 : 0
                if atoms[i][1] > atoms[j][1] and atoms[j][2] == 0 or \
                        atoms[i][1] < atoms[j][1] and atoms[j][2] == 1:
                    d = abs(atoms[i][0] - atoms[j][0])
                    dis.add(d)
                    if (d, j) not in bombs[i]:
                        bombs[i].append((d, j))
                    if (d, i) not in bombs[j]:
                        bombs[j].append((d, i))

            # 방향이 0일때, y좌표는 작고, 이동거리는 같아야 함.
            if atoms[i][1] < atoms[j][1] and atoms[i][2] == 0 and abs(atoms[i][0] - atoms[j][0]) == abs(
                    atoms[i][1] - atoms[j][1]):
                # j 기준: x가 크면 : 2, x가 작으면 : 3
                if atoms[i][0] > atoms[j][0] and atoms[j][2] == 3 or \
                        atoms[i][0] < atoms[j][0] and atoms[j][2] == 2:
                    d = abs(atoms[i][0] - atoms[j][0])
                    dis.add(d)
                    if (d, j) not in bombs[i]:
                        bombs[i].append((d, j))
                    if (d, i) not in bombs[j]:
                        bombs[j].append((d, i))

            # 방향이 1일때, y좌표는 크고, 이동거리는 같아야 함.
            if atoms[i][1] > atoms[j][1] and atoms[i][2] == 1 and abs(atoms[i][0] - atoms[j][0]) == abs(
                    atoms[i][1] - atoms[j][1]):
                # j 기준: x가 크면 : 2, x가 작으면 : 3
                if atoms[i][0] > atoms[j][0] and atoms[j][2] == 3 or \
                        atoms[i][0] < atoms[j][0] and atoms[j][2] == 2:
                    d = abs(atoms[i][0] - atoms[j][0])
                    dis.add(d)
                    if (d, j) not in bombs[i]:
                        bombs[i].append((d, j))
                    if (d, i) not in bombs[j]:
                        bombs[j].append((d, i))

    # 거리가 작은 순으로, 폭탄 터트리기
    dis = list(dis)
    dis.sort()

    # 거리가 작은 것부터 터트린다 !
    for d in dis:
        for n in range(N):
            # 만일 터지지 않은 폭탄이라면
            if not check[n]:
                # 순회하며 거리가 작은 폭탄 터트리기 !
                for m in range(len(bombs[n])):
                    if bombs[n][m][0] == d and not check[bombs[n][m][1]]:
                        result += atoms[bombs[n][m][1]][3] + atoms[n][3]
                        atoms[bombs[n][m][1]][3] = 0
                        atoms[n][3] = 0
                        check[n] = 1
                        check[bombs[n][m][1]] = 1

    print('#{} {}'.format(tc, result))


