# 5176_이진탐색 풀이
# 2022-03-17
import sys
sys.stdin = open('sample_input.txt', 'r')


# tree 만들기
# 중위순회하는 순서대로 1부터 N까지 넣어준다.
def inorder(v):
    global num

    # tree[v]가 입력되지 않은 상태일 때
    if not tree[v]:
        if v*2 <= N:       # 왼쪽 자식으로 이동
            inorder(v*2)
        tree[v] = num      # L > V > R 순으로 차례대로 숫자를 입력
        num += 1
        if v*2+1 <= N:     # 오른쪽 자식으로 이동
            inorder(v*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1

    inorder(1)      # 트리 만들기
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
