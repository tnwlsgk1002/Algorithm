import sys
input = sys.stdin.readline

n = int(input())

MAX = 10001
dp = [0 for _ in range(MAX)]
dp[0] = 1

for i in (1, 2, 3):
  for j in range(i, MAX):
    dp[j] += dp[j-i]

for _ in range(n):
  k = int(input())
  print(dp[k])
  