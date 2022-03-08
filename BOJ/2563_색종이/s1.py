# 2563_색종이 풀이
# 2022-03-09

N = int(input())
area = [[0] * 100 for _ in range(100)]  # 흰 종이 만들기

# 검은 색종이가 있는 위치 1로 바꾼다.
for n in range(N):
    x, y = map(int, input().split())

    for p in range(10):
        for q in range(10):
            area[x+p][y+q] = 1

# 검은 색종이가 있는 넓이 구하기
result = 0
for i in range(100):
    result += area[i].count(1)

print(result)
