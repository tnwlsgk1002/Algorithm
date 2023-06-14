import sys
from itertools import combinations
input = sys.stdin.readline
MAX = 1e9

n = int(input())
ingres = [tuple(map(int, input().split())) for _ in range(n)]

answer = MAX
for i in range(1, n + 1):
  cases = combinations(range(n), i)
  for case in cases:
    s = 1
    b = 0
    for j in range(len(ingres)):
      if j in case:
        s *= ingres[j][0]
        b += ingres[j][1]
    answer = min(answer, abs(s - b))

print(answer)