# 4366_정식이의-은행업무 풀이
# 2022-03-24

import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    two = input()  # 이진법
    three = input()  # 삼진법
    stop = 0
    binary = list()  # 이진법에서 가능한 금액

    # 이진법에서 금액찾기
    for i in range(len(two)):
        if two[i] == '1':
            n = int(two[:i] + '0' + two[i + 1:], 2)
        else:
            n = int(two[:i] + '1' + two[i + 1:], 2)

        binary += [n]

    # 삼진법에서 금액찾기
    for j in range(len(three)):
        if three[j] == '0':
            n1 = int(three[:j] + '1' + three[j + 1:], 3)
            n2 = int(three[:j] + '2' + three[j + 1:], 3)
        elif three[j] == '1':
            n1 = int(three[:j] + '0' + three[j + 1:], 3)
            n2 = int(three[:j] + '2' + three[j + 1:], 3)
        else:
            n1 = int(three[:j] + '0' + three[j + 1:], 3)
            n2 = int(three[:j] + '1' + three[j + 1:], 3)


        # 이진법과 같아지는 삼진법 금액이 있다면, 찾고 끝 !
        for b in binary:
            if n1 == b or n2 == b:
                stop = 1
                print('#{} {}'.format(tc, b))
                break

        if stop == 1:
            break
