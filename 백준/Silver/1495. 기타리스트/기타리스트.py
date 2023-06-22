import sys
input = sys.stdin.readline

# 곡의 갯수: n, 시작 볼륨: s, 최대 볼륨: m
n, s, m = map(int, input().split())
# 각 곡이 시작하기 전에 줄 수 있는 볼륨의 차이
v = list(map(int, input().split()))

answer = -1
dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True

for i in range(n):
  for j in range(m+1):
    if dp[i][j]:
      for x in [j + v[i], j - v[i]]:
        if 0 <= x and x <= m:
          dp[i+1][x] = True

answer = -1
for i in range(m + 1):
  if dp[n][i]:
    answer = max(answer, i)

print(answer)