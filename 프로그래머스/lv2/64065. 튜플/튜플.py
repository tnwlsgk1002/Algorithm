import re

def solution(s):
    
    # 문자열 -> 리스트(집합)로 분리
    # 길이를 기준으로 정렬
    # 차집합으로 없는 값 answer에 넣기
    s = re.findall('{[,*\d+,*]+}', s)
    s = [set(map(int, re.findall('\d+', i))) for i in s]
    s.sort(key = lambda x: len(x))
    
    # answer = set()
    # for i in s:
    #     # print(i)
    #     answer.update(i - answer)
    
    answer = []
    temp = set()
    for i in s:
        ans = i - temp
        answer.extend(list(ans))
        temp.update(ans)
    
    return list(answer)