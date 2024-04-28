import sys
import heapq #minheap tuple first기준 -> first : distance second : node

#N : node , M : edge, X : destination
N,M,X= (map)(int, sys.stdin.readline().split())

graph1=[[] for _ in range(N+1)] #갈 때
graph2=[[] for _ in range(N+1)] #올 떄 , X 기준으로 다익스트라 알고리즘

for _ in range(M) :
    start,end,cost= (map)(int, sys.stdin.readline().split())
    graph1[end].append([cost,start]) # 갈 때
    graph2[start].append([cost,end]) # 올 때 X 기준으로 다익스트라 알고리즘 ->2VlogE

dist1 = [sys.maxsize for _ in range(N+1)] # 갈 때
pq1=[]
heapq.heappush(pq1, (0,X))

#갈 때 기준 다익스트라 알고리즘
while pq1 :
    now = heapq.heappop(pq1)
    now_cost = now[0] 
    now_node = now[1]
    
    if now_cost > dist1[now_node] :
        continue
    
    else :
        #현재 최소 cost로 갱신 후
        dist1[now_node] = now_cost
        
        for node in graph1[now_node] : #i = (cost, end) 
            adj_cost = node[0]
            adj_node = node[1]
            
            if adj_cost + dist1[now_node] < dist1[adj_node] :
                heapq.heappush(pq1,(adj_cost + dist1[now_node],adj_node))

#print(dist1)


#올 때 기준 다익스트라 알고리즘
dist2 = [sys.maxsize for _ in range(N+1)] # 올 때
pq2=[]
heapq.heappush(pq2, (0,X))

while pq2 :
    now = heapq.heappop(pq2)
    now_cost = now[0] 
    now_node = now[1]
    
    if now_cost > dist2[now_node] :
        continue
    #now_cost <= dist2[now_node] 즉, 현재 거리가 기존의 거리보다 짧다면, 유망하다면
    else :
        #현재 최소 cost로 갱신 후
        dist2[now_node] = now_cost
        
        for node in graph2[now_node] : #i = (cost, end) 
            adj_cost = node[0]
            adj_node = node[1]
            
            if adj_cost + dist2[now_node] < dist2[adj_node] :
                heapq.heappush(pq2,(adj_cost + dist2[now_node],adj_node))
#print(dist2)

answer_list=[]
for i in range(1,N+1) :
    answer_list.append(dist1[i]+dist2[i])
    
print(max(answer_list))