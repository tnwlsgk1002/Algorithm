def solution(n, lost, reserve):
    # 여벌 체육복 가져온 학생이 도난당한 경우 제거
    _lost = set(lost)
    _reserve = set(reserve)

    lost = _lost - _reserve
    reserve = _reserve - _lost

    # 앞 -> 뒤 순으로 체육복 빌려주기
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
    
    return n - len(lost)