import sys
input = sys.stdin.readline

a, b = map(int, input().split())

answer = 1

while True:
  if a == b:
    break
  elif a > b:
    answer = -1
    break
  elif b % 10 == 1:
    b //= 10 # 1을 수의 가장 오른쪽에 추가한다. => 나머지가 1인지 확인한다.
    answer += 1
  elif b % 2 == 0:
    b //= 2 # 2를 곱한다 -> b를 2로 나눈다.
    answer += 1
  else:
    answer = -1
    break

print(answer)