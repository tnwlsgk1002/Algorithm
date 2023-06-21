import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  queue = deque()
  queue.append(a)
  while queue:
    x = queue.popleft()

    for nx in [x * 2, int(str(x) + '1')]:
      if nx < a or nx > b or graph.get(nx, -1) != -1:
        continue
      graph[nx] = graph[x] + 1
      queue.append(nx)

  if graph.get(b, -1) != -1:
    return graph[b] + 1
  return -1
  
a, b = map(int, input().split())
graph = dict()
graph[a] = 0

print(bfs())