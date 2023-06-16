import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for value in values:
  for i in range(value, k + 1):
    dp[i] += dp[i-value]
    
print(dp[k])