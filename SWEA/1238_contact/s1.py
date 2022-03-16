# 1238_contact 풀이
# 2022-03-16

import sys
sys.stdin = open('input.txt', 'r')


def bfs(v):
    global connect
    global result

    queue = [[v]]
    visit[v] = 1

    while queue:
        starts = queue.pop()
        val = list()
        for start in starts:
            visit[start] = True

            for i in connect[start]:
                if not visit[i]:
                    visit[i] = 1
                    val.append(i)

        if val:
            queue.append(val)
            result = val       # 연결된 연락망이 존재할 때, 가장 마지막에 연락한 번호들 리스트 저장


T = 10
for tc in range(1, T+1):
    len_data, start_p = map(int, input().split())   # len_data: 데이터의 길이, start_p: 시작점
    data = list(map(int, input().split()))          # data: 연락망 데이터
    connect = [[] for _ in range(101)]              # connect: 연결상태
    visit = [0] * 101                               # visit: 방문 여부 확인
    result = list()                                 # result: 가장 나중에 연락을 받게 되는 사람들 번호

    # 연결상태 저장, 중복제거
    for i in range(0, len_data, 2):
        if data[i+1] not in connect[data[i]]:
            connect[data[i]].append(data[i+1])
        else:
            continue

    bfs(start_p)
    print('#{} {}'.format(tc, max(result)))