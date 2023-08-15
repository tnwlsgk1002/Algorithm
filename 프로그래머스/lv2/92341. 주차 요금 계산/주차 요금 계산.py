from collections import defaultdict
import math
# 기본 시간 이하라면 기본 요금 청구
# fees[0] = 기본 시간(분)
# fees[1] = 기본 요금(원)
# 기본 시간 초과하면 기본 요금 + 단위 요금
# fees[2] = 단위 시간(분)
# fees[3] = 단위 요금(원)
# return: 차량 번호가 작은 순대로 청구할 주차 요금 배열

# 주차 시간 문자열 주면 분 반환

def string_to_time(time):
    return map(int, time.split(':'))

def get_parking_time(in_time, out_time):
    in_hour, in_minute = string_to_time(in_time)
    out_hour, out_minute = string_to_time(out_time)
    return (out_hour - in_hour) * 60 + out_minute - in_minute

                                        
def solution(fees, records):
    # 주차 요금을 딕셔너리로 나타내기
    records_dict = defaultdict(list)
    for record in records:
        r = record.split()
        records_dict[r[1]].append(r[0])
    
    # 각 번호별 요금 정산
    # 주차 시간, 주차 요금 반환
    def get_fee(parking_time):
        # 기본 요금 추가
        ans = fees[1]
        # 만약 기본 시간을 초과하면 ans에 추가 요금 계산
        if fees[0] < parking_time:
            ans += math.ceil((parking_time - fees[0]) / fees[2]) * fees[3]
        return ans
    
    answer = defaultdict(int)
    
    for n, times in records_dict.items():
        # IN -> (OUT) 순서
        parking_time = 0
        for i in range(0, len(times), 2):
            in_time = times[i]
            out_time = times[i+1] if i != len(times) - 1 else "23:59"
            parking_time += get_parking_time(in_time, out_time)
        answer[n] += get_fee(parking_time)
            
    # 차량번호가 작은 순으로 정렬
    answer = sorted(answer.items(), key = lambda x: x[0])
    
    return [a[1] for a in answer]