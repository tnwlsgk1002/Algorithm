def solution(d_list, budget):
    # 최대한 많은 부서의 물품 구매
    # 신청한 금액만큼 지원
    # 1000원 신청 <- 1000원 지원
    d_list.sort()
    answer = 0
    for d in d_list:
        budget -= d
        if budget >= 0 :
            answer += 1
        else:
            break
    return answer