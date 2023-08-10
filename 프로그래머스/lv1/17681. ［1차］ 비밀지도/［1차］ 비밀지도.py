def solution(n, arr1, arr2):
    answer = [bin(a | b) for a, b in zip(arr1, arr2)]
    
    for i, s in enumerate(answer):
        ans = s.lstrip('0b').zfill(n)
        answer[i] = ''.join(['#' if '1' == a else ' ' for a in ans])
    return answer