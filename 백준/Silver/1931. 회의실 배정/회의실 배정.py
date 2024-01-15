import sys,heapq

n = (int)(input())

time_table = []

for _ in range(n) :
    start, end = (map)(int, sys.stdin.readline().split())
    time = (end, start) #끝나는 시간 기준 정렬 minheap
    heapq.heappush(time_table, time)

end_time =0
answer=0

while time_table :
    now_plan = heapq.heappop(time_table)
    now_plan_start_time = now_plan[1]
    now_plan_end_time = now_plan[0]
    
    if now_plan_start_time >= end_time :
        answer+=1
        end_time = now_plan_end_time
    else :
        #타임 테이블이 존재하면서, 현재 시작 시간이 기존의 끝 시간보다 작다면
        while time_table :
            if now_plan_start_time >=end_time :
                break
            now_plan = heapq.heappop(time_table)
            now_plan_start_time = now_plan[1]
            now_plan_end_time = now_plan[0]
        if now_plan_start_time >= end_time :
            answer+=1
            end_time = now_plan_end_time
print(answer)    
