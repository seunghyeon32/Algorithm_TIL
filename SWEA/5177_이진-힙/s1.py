# 5177_이진-힙 풀이
# 2022-03-21
import sys
sys.stdin = open('sample_input.txt', 'r')


# 최소 힙 만들면서 추가하기
def enq(n):
    global last
    last += 1           # 길이 +1
    tree[last] = n      # 마지막 노드에 숫자 저장

    c = last            # 숫자를 추가한 노드(자식노드)
    p = c//2            # 부모노드

    while p > 0 and tree[p] > tree[c]:  # 부모가 있고, 자식의 키 값이 더 작으면
        tree[p], tree[c] = tree[c], tree[p]   # 부모와 자식 교환

        # 위의 과정을 반복하기 위해 부모와 자식의 값을 수정해줌.
        # 만일, 부모의 값이 자식의 값보다 작아지거나 부모노드가 없을 때 반복문은 멈추게 된다.
        c = p
        p = c//2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    val = list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 0

    for v in val:
        enq(v)

    n = N
    result = 0

    # 마지막 노드의 조상노드의 합 구하기
    while n > 0:
        n = n//2
        result += tree[n]

    print('#{} {}'.format(tc, result))
