def solution(board):
    answer = set() # 위험한 지역
    n = len(board)
    dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    for x, i in enumerate(board):
        for y, j in enumerate(i):
            if j == 1:
                for k in range(9):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        answer.add((nx, ny))
    return n * n - len(answer)