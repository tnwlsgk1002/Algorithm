import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001

def bfs(x):
  global count
  queue = deque()
  queue.append(x)
  
  while queue:
    x = queue.popleft()
    if x == k:
      count += 1
    for m in (x - 1, x + 1, x * 2):
      if m < 0 or m >= MAX:
        continue
      if graph[m] == -1 or graph[m] >= graph[x] + 1:
        graph[m] = graph[x] + 1
        queue.append(m)
        
  return graph[k]

n, k = map(int, input().split())
graph = [-1 for _ in range(MAX)]
graph[n] = 0
count = 0

print(bfs(n))
print(count)