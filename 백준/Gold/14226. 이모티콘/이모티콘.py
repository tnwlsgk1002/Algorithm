import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  queue = deque()
  queue.append((1, 0))
  # 스크린에 있는 이모티콘 갯수(복사 or 지우기 가능) / 클립보드에 있는 이모티콘 갯수(붙여넣기 가능)
  while queue:
    screen, clip = queue.popleft()
    # 1. 화면에 있는 이모티콘을 복사해서 저장
    if screen > 0 and screen < s + 1 and graph[screen][screen] == -1:
      graph[screen][screen] = graph[screen][clip] + 1
      queue.append((screen, screen))
    # 2. 클립 보드에 있는 모든 이모티콘을 화면에 붙여넣기
    if screen > 0 and screen < s + 1 and clip > 0 and clip < s + 1 and screen + clip < s + 1 and graph[screen + clip][clip] == -1:
      graph[screen + clip][clip] = graph[screen][clip] + 1
      queue.append((screen + clip, clip))
    # 3. 화면에 있는 이모티콘 중 하나를 삭제
    if screen - 1 > 0 and screen < s + 1 and graph[screen - 1][clip] == -1:
      graph[screen - 1][clip] = graph[screen][clip] + 1
      queue.append((screen - 1, clip))

  result = graph[s][1]
  for i in range(1, s):
    if graph[s][i] != -1:
      result = min(result, graph[s][i])
  return result
  
s = int(input())

graph = [[-1] * (s + 1) for _ in range(s+1)]
graph[1][0] = 0 # graph[화면에 있는 이모티콘 갯수][클립보드에 있는 이모티콘 갯수]

print(bfs())