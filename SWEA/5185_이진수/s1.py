# 5185_이진수 풀이
# 2022-03-24
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, nums = map(str, input().split())
    N = int(N)
    binary = ''
    for n in range(N):
        num = int(nums[n], 16)                                  # 16진수를 10진수로
        binary += '0' * (4 - len(bin(num)[2:])) + bin(num)[2:]   # 10진수를 2진수로

    print('#{} {}'.format(tc, binary))