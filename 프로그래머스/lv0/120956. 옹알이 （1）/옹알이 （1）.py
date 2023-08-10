from itertools import permutations

def solution(babbling):
    babbling_set = set()
    for i in range(1, 5):
        babbling_set.update([''.join(j) for j in list(permutations(['aya', 'ye', 'woo', 'ma'], i))])
    
    answer = 0
    for b in babbling:
        if b in babbling_set:
            answer += 1
    return answer