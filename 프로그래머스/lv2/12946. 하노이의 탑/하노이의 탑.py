def solution(n):
    answer = []
    
    # n - 1개의 원판을 출발 기둥 -> 중간 기둥 이동
    # n번째 원판을 출발 -> 도착 이동
    # n - 1개의 원판을 중간 -> 도착 기둥 이동
    
    '''
    @param
    n : 옮겨야 하는 원판 갯수
    from_pos : 출발 기둥
    to_pos : 도착 기둥
    mid_pos : 중간 기둥
    '''
    def hanoi(n, from_pos, to_pos, mid_pos):
        # 원반이 한 개일 때 : 출발 -> 도착 기둥 이동
        if n == 1:
            answer.append([from_pos, to_pos])
        else:
            # 1. n - 1개의 원판을 출발 기둥 -> 중간 기둥 이동
            hanoi(n - 1, from_pos, mid_pos, to_pos)
            # 2. n 번째 원판을 출발 기둥 -> 도착 기둥 이동
            hanoi(1, from_pos, to_pos, mid_pos)
            # 3. n - 1개의 원판을 중간 기둥 -> 도착 기둥으로 이동
            hanoi(n - 1, mid_pos, to_pos, from_pos)
    
    hanoi(n, 1, 3, 2)
    return answer