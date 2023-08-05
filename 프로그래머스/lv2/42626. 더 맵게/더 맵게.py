import heapq

def maxheap(minheap, K) :
    maxheap = []
    for num in minheap :
        heapq.heappush(maxheap, -num)
    first = heapq.heappop(maxheap)
    second = heapq.heappop(maxheap)
    item = first + second * 2
    if K > (-item) :
        return -1
    return 0
    
def solution(scoville, K):
    # scoville = [1,2,3,9,10,12]
    # K = 7
    heapq.heapify(scoville)
    #answer = maxheap(scoville, K)
    answer = 0
    while scoville[0] < K :
        if len(scoville) == 1 :
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        item = first + second * 2
        heapq.heappush(scoville, item)
        answer += 1

    return answer