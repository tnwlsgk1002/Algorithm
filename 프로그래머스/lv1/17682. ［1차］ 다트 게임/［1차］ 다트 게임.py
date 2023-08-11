import re

def solution(dartResult):
    # Single, Double, Triple
    # 1제곱, 2제곱, 3제곱
    # 스타상(*) -> 해당 점수 + 전의 점수를 각 2배로 만듬
    # 스타상은 첫번째 기회도 나올 수 있으므로 이때는 첫번째만 두배
    # 다른 스타상 효과와 중첩 가능
    # 아차상(#) -> 해당 점수는 마이너스
    # Single, Double, Triple -> 점수마다 하나씩
    # 스타상, 아차상 -> 점수마다 둘 중 하나만 혹은 존재 X
    p = re.compile("(\d+)([a-zA-z])(\*|#)?")
    scores = p.findall(dartResult)
    answer = []
    for i, (score, bonus, option) in enumerate(scores):
        score = int(score)
        if bonus == 'S':
            score = score ** 1 # 생략 가능
        elif bonus == 'D':
            score = score ** 2
        else:
            score = score ** 3
        
        if option == '*':
            score *= 2
            if i != 0:
                answer[i-1] *= 2
        elif option == '#':
            score *= -1
            # if i != 0:
            #     answer[i-1] *= -2
        answer.append(score)
    
    print(answer)
    return sum(answer)