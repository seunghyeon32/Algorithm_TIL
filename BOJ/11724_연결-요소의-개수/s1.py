# 11724 연결 요소의 개수

N, M = map(int, input().split())
arr = [0] * (N+1)
group = {}
k = 0
result = 0

for _ in range(M):
    a, b = map(int, input().split())

    if not arr[a] and not arr[b]:   # 두 정점 모두 정보 X
        k += 1
        arr[a], arr[b] = k, k
        group[k] = [a, b]

    # 이미 연결되어 있는 경우
    elif arr[a] == arr[b]:
        continue

    # a만 정보가 있는 경우
    elif arr[a] and not arr[b]:
        tmp = arr[a]
        arr[b] = tmp
        group[tmp].append(b)

    # b만 정보가 있는 경우
    elif arr[b] and not arr[a]:
        tmp = arr[b]
        arr[a] = tmp
        group[tmp].append(a)
    else:
        tmp = arr[b]

        # 인접한 노드 모두 바꾸기
        for n in range(N+1):
            if arr[n] == tmp:
                arr[n] = arr[a]

        group[arr[a]].extend(group[tmp])
        group.pop(tmp)

result += len(group)
result += arr.count(0) - 1

print(group, arr)
print(result)